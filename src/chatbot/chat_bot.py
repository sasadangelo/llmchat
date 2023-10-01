# ChatBOT - the ChaatBOT maain class.
#
# This class represents a generic chatbot. It is composed by:
# - a model
# - a chat history
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
from enum import Enum
from langchain.schema import (AIMessage, HumanMessage)
from src.chatbot.conversation import Conversation
from src.models.llama_model import LlamaModel
from src.models.chatgpt_model import ChatGPT35Model, ChatGPT40Model

# This class represents a ChatBOT composed by:
# - chat history
# - the LLM model used to generate the AI answers
class ChatBOT:
    # Here the list of supported LLM models
    class Model(Enum):
        LLAMA = "llama"
        CHATGPT_3_5 = "chatgpt3.5"
        CHATGPT_4 = "chatgpt4"

    # By default, the ChatBOT uses the LLama 2 model and a temperature 0 that means answer more focused
    #  and choerent
    def __init__(self):
        self.model = LlamaModel(0.0)
        self.conversation = Conversation()

    # The user can change the default model with others supportedd.
    def set_model(self, model_type, temperature):
        if model_type == self.Model.LLAMA:
            self.model = LlamaModel(temperature)
        elif model_type == self.Model.CHATGPT_3_5:
            self.model = ChatGPT35Model(temperature)
        elif model_type == self.Model.CHATGPT_4:
            self.model = ChatGPT40Model(temperature)
        else:
            raise ValueError("Invalid model type")

    # Once the user insert the question, this method is called to generate the answer.
    # It leverages on the model get_answer method.
    def get_answer(self, user_input):
        self.conversation.add_message(HumanMessage(content=user_input))
        answer, cost = self.model.get_answer(self.conversation.get_messages())
        self.conversation.add_message(AIMessage(content=answer))
        self.conversation.add_cost(cost)
        return answer, cost

    # Return the chat history
    def get_chat_history(self):
        return self.conversation.get_messages()

    # Return the chat costs
    def get_chat_costs(self):
        return self.conversation.get_costs()

    # Clear the conversation
    def clear_conversation(self):
        self.conversation.clear()
