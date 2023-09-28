# models/base_model.py
class BaseModel:
    def __init__(self, temperature, model_name):
        super().__init__()
        self.model_name = model_name
        self.temperature = temperature

    def get_answer(self, messages) -> tuple[str, float]:
        # Common logic for generating a response
        pass