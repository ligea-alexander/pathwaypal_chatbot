import pandas as pd
docs = pd.read_csv("notebooks/cleaned_scraped_database.csv")
docs

# Fill NaNs with an empty string
docs.fillna("", inplace=True)
documents = docs.to_dict(orient='records')
documents
# import MiniSearch from minisearch
import minsearch
from minsearch import Index

index = Index(
    text_fields=["parent_page", "child_page", "grandchild_page", "great_grandchild_page", "content", "link_type", "link_title"],
    keyword_fields=[]
)

index.fit(documents)
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv() 
import os
client = OpenAI()
query = "what is NEST?"
index.search(query, num_results = 5)
response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{"role": "user", "content": query}]
)

response.choices[0].message.content
query = "when is the next Nest training?"
index.search(query, num_results = 5)
response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{"role": "user", "content": query}]
)

response.choices[0].message.content
documents[0]
def search(query):
    boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results
prompt_template = """
You are a CEO participant. Answer the QUESTION based on the CONTEXT from our scraped NEST website database warehouse.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

entry_template = """
'parent_page': {parent_page},
'child_page':{child_page},
'grandchild_page':{grandchild_page},
'great_grandchild_page':{great_grandchild_page},
'content':{content},
'is_link':{is_link}
'link_type':{link_type},
'link_title':{link_title}
""".strip()


def build_prompt(query, search_results, max_tokens=3000):
    context = ""
    token_count = 0

    for doc in search_results:
        # Estimate the token size of the current entry
        entry = entry_template.format(**doc)
        entry_tokens = len(entry.split())

        # Check if adding this entry exceeds the max tokens limit
        if token_count + entry_tokens > max_tokens:
            break

        context += entry + "\n\n"
        token_count += entry_tokens

    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt
search_results = search(query)
prompt = build_prompt(query, search_results)
# print(prompt)
def llm(prompt):
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{"role": "user", "content": prompt}],
        max_tokens = 1000
    )
    
    return response.choices[0].message.content
def rag(query):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer
answer = rag(query)
print(answer)

# Only the testing code should be under this
if __name__ == '__main__':
    query = "What is NEST?"
    answer = rag(query)
    print(answer)