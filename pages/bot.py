import streamlit as st
st.set_page_config("AgroMate", page_icon=":plant:")
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Shortcut Button to Homepage
if st.button("🏠 Go to Home"):
    st.switch_page("main.py")  

from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
import boto3
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_neo4j import Neo4jChatMessageHistory
from langchain_openai import ChatOpenAI

# Function to write chat messages
def write_message(role, content, save=True):
    if save:
        st.session_state.messages.append({"role": role, "content": content})
    with st.chat_message(role):
        st.markdown(content)

def get_session_id():
    return get_script_run_ctx().session_id

# Initialize OpenAI model
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo",
)

# AWS Configuration
REGION = "eu-north-1"
s3_client = boto3.client("s3", region_name=REGION)

def get_memory(session_id):
    return Neo4jChatMessageHistory(session_id=session_id)

# Chatbot Integration
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an agricultural expert providing information about farming, plant diseases, and precautions."),
    ("human", "{input}")
])

agriculture_chat = chat_prompt | llm | StrOutputParser()

def generate_response(user_input):
    response = agriculture_chat.invoke({"input": user_input})
    return response

st.subheader("\U0001F4AC Chat with the Agricultural Expert")

# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the AgroMate Chatbot! How can I help you?"},
    ]

# Submit handler
def handle_submit(message):
    with st.spinner("Thinking..."):
        response = generate_response(message)
        write_message("assistant", response)

# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if question := st.chat_input("What is up?"):
    write_message('user', question)
    handle_submit(question)