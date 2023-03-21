# GPT-4 Chatbot

A simple chatbot using GPT-4 and Streamlit to generate interactive conversations.

## Prerequisites

- Python 3.10 used
- Create virtual env
- Install the required packages using the following command:
```
pip install openai streamlit streamlit-chat
```

## Active venv
```
source .venv/Scripts/activate
```

## Configuration

- Obtain an OpenAI API key: [https://beta.openai.com/signup/](https://beta.openai.com/signup/)
- Replace `your_api_key` with your OpenAI API key:
```python
openai.api_key = "your_api_key"
```

## Running the Chatbot

Run the following command in your terminal:

```
streamlit run file.py
```

Replace `script_name.py` with the name of your chatbot script.

## Usage

You will see a web interface with a text area to type your input, and a send button to submit your input to the chatbot. The chatbot will generate a response, and the conversation will be displayed on the screen.

## Code Overview

- Import necessary libraries:
```python
import openai
import streamlit as st
from streamlit_chat import message
```

- Setup OpenAI API key:
```python
openai.api_key = "your_api_key"
```

- Define `generate_response()` function to get response from GPT-4 model:
```python
def generate_response(prompt):
...
return message
```

- Streamlit UI setup:
```python
st.title("Gpt-4 Chatbot")
```

- Store the chat history:
```python
if 'generated' not in st.session_state:
st.session_state['generated'] = []
if 'past' not in st.session_state:
st.session_state['past'] = []
```

- Create containers for chatbot responses and user inputs:

```python
response_container = st.container()
container = st.container()
```

- Add user input form with submit button, and handle the form submission:

```python
with container:
with st.form(key='my_form'):
...
if submit_button and user_input:
...
```

- Display chatbot responses:

```python
if st.session_state['generated']:
with response_container:
...
```

- Hide Streamlit menu and footer:

```python {
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
```