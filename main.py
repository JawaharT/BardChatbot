from bardapi import BardCookies
import streamlit as st
from streamlit_chat import message
import os

cookie_dict = {
    "__Secure-1PSID": "",
    "__Secure-1PSIDTS": "",
    "__Secure-1PSIDCC":""
}

# cookie_dict = {
#     "__Secure-1PSID": os.environ.get("secure-1PSI"),
#     "__Secure-1PSIDTS": os.environ.get("secure-1PSIDTS"),
#     "__Secure-1PSIDCC": os.environ.get("secure-1PSIDCC"),
# }

if 'generate' not in st.session_state:
    st.session_state['generate']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

bard = BardCookies(cookie_dict=cookie_dict)
#message = input("Enter your prompt: ")
#print(bard.get_answer(message)['content'])

st.title("Google Bard Chatbot")

def response_api(prompt):
    message = bard.get_answer(prompt)['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Prompt: ")
    return input_text

user_text = user_input()
if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.generate.append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + "_user")
        message(st.session_state['generate'][i], key=str(i))
        