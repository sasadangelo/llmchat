# models/chatgpt_model.py
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from src.models.base_model import Model

class ChatGPTModel(Model):
    def __init__(self, temperature, model_name):
        super().__init__(temperature, model_name)
        self.model = ChatOpenAI(temperature=temperature, model_name=model_name)

    def get_answer(self, messages) -> tuple[str, float]:
        with get_openai_callback() as cb:
            answer = self.model(messages)
        return answer.content, cb.total_cost

class ChatGPT35Model(ChatGPTModel):
    def __init__(self, temperature):
        super().__init__(temperature, "gpt-3.5-turbo-0613")

class ChatGPT40Model(ChatGPTModel):
    def __init__(self, temperature):
        super().__init__(temperature, "gpt-4")
