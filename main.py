from bardapi import BardCookies
import streamlit as st
from streamlit_chat import message

# cookies stored in this dictionary
cookie_dict = {
    "__Secure-1PSID": "XXXXXXXX",
    "__Secure-1PSIDTS": "XXXXXXXX",
    "__Secure-1PSIDCC": "XXXXXXXX"
}

# Streamlit session state to store the chat converations
if 'generate' not in st.session_state:
    st.session_state['generate'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# bard object creation
bard = BardCookies(cookie_dict=cookie_dict)

st.title("Google Bard Chatbot")

# get bard response
def response_api(prompt):
    message = bard.get_answer(prompt)['content']
    return message

# get user prompt
def user_input():
    input_text = st.text_input("Enter Your Prompt: ")
    return input_text

user_text = user_input()

# if user prompt provided add to session state of Streamlit app
if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

# show message to user after bard response generated
if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + "_user")
        message(st.session_state['generate'][i], key=str(i))
        