# app.py
from typing import List, Union
from dotenv import load_dotenv, find_dotenv
import streamlit as st
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)
from src.models.base_model import Model
from src.models.chatgpt_model import ChatGPT35Model, ChatGPT40Model
from src.models.llama_model import LlamaModel

def init_page() -> None:
    st.set_page_config(
        page_title="MyChatBOT"
    )
    st.header("MyChatBOT")
    st.sidebar.title("Options")

def init_messages() -> None:
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(
                content="You are a helpful AI assistant. Reply your answer in mardkown format.")
        ]
        st.session_state.costs = []

def select_model() -> Model:
    model_name = st.sidebar.radio("Choose LLM:", ("Llama 2.0", "GPT 3.5", "GPT 4.0"))
    temperature = st.sidebar.slider("Coherent <-> Creative:", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    if model_name == "GPT 3.5":
        return ChatGPT35Model(temperature)
    elif model_name == "GPT 4.0":
        return ChatGPT40Model(temperature)
    elif model_name == "Llama 2.0":
        return LlamaModel(temperature)

def main() -> None:
    _ = load_dotenv(find_dotenv())

    init_page()
    model = select_model()
    init_messages()

    # Supervise user input
    if user_input := st.chat_input("Input your question!"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            answer, cost = model.get_answer(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=answer))
        st.session_state.costs.append(cost)

    # Display chat history
    messages = st.session_state.get("messages", [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)

    costs = st.session_state.get("costs", [])
    st.sidebar.markdown("## Costs")
    st.sidebar.markdown(f"**Total cost: ${sum(costs):.5f}**")
    for cost in costs:
        st.sidebar.markdown(f"- ${cost:.5f}")

# streamlit run app.py
if __name__ == "__main__":
    main()
