from dotenv import load_dotenv
import streamlit as st
from langchain_ollama import ChatOllama

load_dotenv()
st.set_page_config(
    page_title="chatbot",
    page_icon= "🤖",
    layout="centered"
)
st.title("💬 Generative AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatOllama(
    model="llama3.1:latest",
    temperature= 0.0

)

user_input = st.chat_input("Ask anything....")
if user_input:
    st.chat_message("user").markdown(user_input)

    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = llm.invoke(
        input=[{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)