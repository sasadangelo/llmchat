# models/chatgpt_model.py
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from base_model import BaseModel

class ChatGPTModel(BaseModel):
    def __init__(self, temperature, model_name):
        super().__init__(temperature, model_name)
        self.model = ChatOpenAI(temperature=temperature, model_name=model_name)


    def get_answer(self, messages) -> tuple[str, float]:
        with get_openai_callback() as cb:
            answer = self.model(messages)
        return answer.content, cb.total_cost
