import streamlit as st
from pathway_pal import rag  # Make sure this function is importable
import logging

# Configure logging only once; choose the format you prefer
logging.basicConfig(filename='chatbot_logs.log', level=logging.INFO,
                    format='%(asctime)s - USER: %(user)s - QUERY: %(query)s - ANSWER: %(answer)s')

def log_interaction(query, answer, user="test_user"):
    # Log the user query and the chatbot's response
    logging.info('USER: %s - QUERY: %s - ANSWER: %s', user, query, answer)

def main():
    st.title("PathwayPal Chatbot")
    
    # User query input
    query = st.text_input("Ask me something about CEO's NEST or Advanced Training:")
    
    if st.button("Submit"):
        if query:
            # Use the rag function from pathway_pal.py to get the answer
            answer = rag(query)
            st.write("Answer:", answer)

            # Log the query and the answer
            log_interaction(query, answer)
        else:
            st.error("Please enter a query to get an answer.")

if __name__ == '__main__':
    main()
