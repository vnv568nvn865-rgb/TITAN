# واجهة النموذج اللغوي في TITAN

class LLM:
    def __init__(self, model_name="local"):
        self.model_name = model_name

    def generate(self, prompt):
        raise NotImplementedError(
            "لم يتم ربط نموذج لغوي بعد."
        )

    def is_available(self):
        return False

    def get_model_name(self):
        return self.model_name
