import streamlit as st
from pathway_pal import rag  # Make sure this function is importable

def main():
    st.title("PathwayPal Chatbot")
    
    # User query input
    query = st.text_input("Ask me something about CEO's NEST or Advanced Training:")
    
    if st.button("Submit"):
        if query:
            # Use the rag function from pathway_pal.py to get the answer
            answer = rag(query)
            st.write("Answer:", answer)
        else:
            st.error("Please enter a query to get an answer.")

if __name__ == '__main__':
    main()
