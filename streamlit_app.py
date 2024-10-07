import streamlit as st
from pathway_pal import rag  # Assuming this function handles the chatbot interaction

def main():
    st.title("PathwayPal Chatbot")

    # Initialize session state if not already initialized
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # User query input
    query = st.text_input("Ask me something about CEO's NEST or Advanced Training:")

    if st.button("Submit"):
        if query:
            # Use the rag function to get the chatbot's answer
            answer = rag(query)

            # Display the answer using markdown to render the clickable link
            st.markdown(answer, unsafe_allow_html=False)

            # Append the interaction to the chat history
            st.session_state.chat_history.append(f"Query: {query}\nAnswer: {answer}\n{'-'*40}\n")

            # Optionally, display the chat history in the app using text_area for scrolling
            st.text_area("Chat History", value=''.join(st.session_state.chat_history), height=250)
        else:
            st.error("Please enter a query to get an answer.")

    # Button to download the chat history
    if st.button("Download Chat History"):
        chat_history_str = ''.join(st.session_state.chat_history)
        st.download_button(label="Download as Text File",
                           data=chat_history_str,
                           file_name='chat_history.txt',
                           mime='text/plain')

if __name__ == '__main__':
    main()
