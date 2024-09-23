# PathwayPal ChatBot

## Overview
PathwayPal ChatBot is an interactive tool designed to provide information and support to participants of the NEST program. By leveraging a combination of data from the NEST website and advanced AI techniques, PathwayPal offers users answers to common questions about training schedules, services, and resources available through NEST.

## Features
- **Interactive Q&A:** Users can ask questions and receive accurate, context-aware responses.
- **Integration with OpenAI's GPT-4:** Utilizes the latest advancements in AI to ensure responses are relevant and informative.
- **Local Search Optimization:** Employs Minsearch to efficiently search through local datasets for relevant information.

## Technologies
- Python
- Pandas for data manipulation
- Minsearch for indexing and searching local data
- OpenAI API for generating responses
- Streamlit for the web interface

## Getting Started

### Prerequisites
- Python 3.8 or higher
- An API key from OpenAI
- Streamlit

### Installation
1. Clone the repository:
   ```bash
   git clone [URL to your repository]
   cd [repository name]
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
3. Set up the environment variables:
* Ensure you have a .env file in your root directory with your OpenAI API key:
    ```bash
    OPENAI_API_KEY='your_openai_api_key_here'


### Running the Application
Start the Streamlit interface:
    ```streamlit run streamlit_app.py
    ```


### Usage
* Open your web browser to the address shown in your terminal (usually http://localhost:8501).
* Use the text input box to ask questions about the NEST program.
* View the responses directly in the browser.

### Development
To contribute to the development of PathwayPal, please create a branch and submit pull requests for review.

### License
Specify the license under which your project is made available (e.g., MIT, GPL).