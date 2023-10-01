# ChatBotPage - Display the ChatBot page
#
# This class is responsible for displaying the ChatBot page using Streamlit.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
import streamlit as st
from langchain.schema import (HumanMessage, AIMessage)
from src.models.base_model import Model
from src.ui.page import Page
from src.chatbot.chat_bot import ChatBOT

# This class is responsible for displaying the ChatBOT page using Streamlit.
class ChatBotPage(Page):
    # Renders the ChatBOT page.
    def render(self):
        # Initialize the page with the title, header, and sidebar.
        self.__init_page()
        # Select the LLM model to use.
        self.__select_model()
        # Initialize the conversation.
        self.__init_messages()

        # Supervise user input
        if user_input := st.chat_input("Input your question!"):
            with st.spinner("LLM ChatBOT is typing ..."):
                _, _ = st.session_state.chatbot.get_answer(user_input)

        # Display chat history
        messages = st.session_state.chatbot.get_chat_history()
        for message in messages:
            if isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)

        # Display the chat cost
        costs = st.session_state.chatbot.get_chat_costs()
        st.sidebar.markdown("## Costs")
        st.sidebar.markdown(f"**Total cost: ${sum(costs):.5f}**")
        for cost in costs:
            st.sidebar.markdown(f"- ${cost:.5f}")

    # Initialize the ChatBOT page
    def __init_page(self) -> None:
        st.set_page_config(
            page_title="LLM ChatBOT"
        )
        st.header("LLM ChatBOT")
        st.sidebar.title("Options")
        if "chatbot" not in st.session_state:
            chatbot = ChatBOT()
            st.session_state.chatbot = chatbot

    # Select the ChatBOT LLM model
    def __select_model(self) -> Model:
        model_name = st.sidebar.radio("Choose LLM model:", ("Llama 2.0", "GPT 3.5", "GPT 4.0"))
        temperature = st.sidebar.slider("Coherent <-> Creative:", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
        if model_name.lower() == "gpt 3.5":
            st.session_state.chatbot.set_model(ChatBOT.Model.CHATGPT_3_5, temperature)
        elif model_name.lower() == "gpt 4.0":
            st.session_state.chatbot.set_model(ChatBOT.Model.CHATGPT_4_0, temperature)
        elif model_name.lower() == "llama 2.0":
            st.session_state.chatbot.set_model(ChatBOT.Model.LLAMA, temperature)

    # Clear the conversation
    def __init_messages(self) -> None:
        clear_button = st.sidebar.button("Clear Conversation", key="clear")
        if clear_button:
            st.session_state.chatbot.clear_conversation()
