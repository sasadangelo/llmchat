# ui/app.py
import streamlit as st
from models.base_model import BaseModel
from models.llama_model import LlamaModel
from models.chatgpt_model import ChatGPTModel

def init_page() -> None:
    st.set_page_config(
        page_title="Personal ChatGPT"
    )
    st.header("Personal ChatGPT")
    st.sidebar.title("Options")

def init_messages() -> None:
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(
                content="You are a helpful AI assistant. Reply your answer in mardkown format.")
        ]
        st.session_state.costs = []

def main() -> None:
    init_page()
    model_type = st.sidebar.radio("Choose Model Type:", ("LLAME2", "ChatGPT"))
    
    if model_type == "LLAME2":
        model = LlamaModel()
    elif model_type == "ChatGPT":
        model = ChatGPTModel()
    
    init_messages()
    
    if user_input := st.chat_input("Input your question!"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            answer, cost = model.generate_response(st.session_state.messages)
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

if __name__ == "__main__":
    main()
