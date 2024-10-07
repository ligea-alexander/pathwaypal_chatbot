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

            # Check for URLs and make them clickable
            if "http://" in answer or "https://" in answer:
                answer = make_clickable(answer)

            # Display the answer using markdown to allow HTML content
            st.markdown(answer, unsafe_allow_html=True)

            # Append the interaction to the chat history, converting URLs in history as well
            formatted_answer = make_clickable(answer)
            st.session_state.chat_history.append(f"Query: {query}\nAnswer: {formatted_answer}\n{'-'*40}\n")

            # Optionally, display the chat history in the app using markdown
            st.markdown(''.join(st.session_state.chat_history), unsafe_allow_html=True, height=250)
        else:
            st.error("Please enter a query to get an answer.")

    # Button to download the chat history
    if st.button("Download Chat History"):
        chat_history_str = ''.join(st.session_state.chat_history)
        st.download_button(label="Download as Text File",
                           data=chat_history_str,
                           file_name='chat_history.txt',
                           mime='text/plain')

def make_clickable(text):
    """Converts URLs in text to HTML anchor tags."""
    import re
    # This regex finds all occurrences of URLs
    url_pattern = re.compile(r'(https?://\S+)')
    # Replace all URLs with an anchor tag
    text = url_pattern.sub(r'<a href="\1" target="_blank">\1</a>', text)
    return text

if __name__ == '__main__':
    main()
