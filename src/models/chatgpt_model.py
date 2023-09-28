# models/chatgpt_model.py
from models.base_model import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback

class ChatGPTModel(BaseModel):
    def __init__(self, model_name="gpt-3.5-turbo-0613"):
        super().__init__()
        self.chat_openai = ChatOpenAI(temperature=0.0, model_name=model_name)

    def generate_response(self, messages):
        with get_openai_callback() as cb:
            answer = self.chat_openai(messages)
        return answer.content, cb.total_cost
