import openai
import streamlit as st
from streamlit_chat import message
import os

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_response(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )
    message=completion.choices[0].message.content
    return message

def load_css():
    with open("./assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()    

st.markdown("<h1 style='text-align: center;'>GPT-4 Answer</h1>", unsafe_allow_html=True)
#storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# create a container for the chatbot responses
response_container = st.container()

# create a container for the user input
container = st.container()

# add a form to the container
with container:
    with st.form(key='my_form'):
        # add a submit button
        submit_button = st.form_submit_button(label='Ask to GPT-4')

        # add a text input
        user_input = st.text_area("You:", key='input',height=200)
    
    # check if the submit button is clicked
    if submit_button and user_input:
        output = generate_response(user_input)
        # store the output
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

# display the chatbot responses
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
