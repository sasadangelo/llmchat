# chatbot.py
from enum import Enum
from langchain.schema import (AIMessage, HumanMessage)
from src.chatbot.conversation import Conversation
from src.models.llama_model import LlamaModel
from src.models.chatgpt_model import ChatGPT35Model, ChatGPT40Model

class ChatBOT:
    class Model(Enum):
        LLAMA = "llama"
        CHATGPT_3_5 = "chatgpt3.5"
        CHATGPT_4 = "chatgpt4"

    def __init__(self):
        self.model = LlamaModel(0.0)
        self.conversation = Conversation()

    def set_model(self, model_type, temperature):
        if model_type == self.Model.LLAMA:
            self.model = LlamaModel(temperature)
        elif model_type == self.Model.CHATGPT_3_5:
            self.model = ChatGPT35Model(temperature)
        elif model_type == self.Model.CHATGPT_4:
            self.model = ChatGPT40Model(temperature)
        else:
            raise ValueError("Invalid model type")

    def get_answer(self, user_input):
        self.conversation.add_message(HumanMessage(content=user_input))
        answer, cost = self.model.get_answer(self.conversation.get_messages())
        self.conversation.add_message(AIMessage(content=answer))
        self.conversation.add_cost(cost)
        return answer, cost

    def get_chat_history(self):
        return self.conversation.get_messages()

    def get_chat_costs(self):
        return self.conversation.get_costs()

    def clear_conversation(self):
        self.conversation.clear()
