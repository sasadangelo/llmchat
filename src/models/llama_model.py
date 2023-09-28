# models/llama_model.py
from models.base_model import BaseModel
from langchain.llms import LlamaCpp

class LlamaModel(BaseModel):
    def __init__(self, model_path="./models/llama-2-7b-chat.ggmlv3.q2_K.bin"):
        super().__init__()
        self.llama = LlamaCpp(
            model_path=model_path,
            input={"temperature": 0.0, "max_length": 2000, "top_p": 1},
            verbose=False,
        )

    def generate_response(self, messages):
        llama_input = llama_v2_prompt(convert_langchainschema_to_dict(messages))
        return self.llama(llama_input), 0.0
