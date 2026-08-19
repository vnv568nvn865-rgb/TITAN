# النموذج اللغوي الأساسي في TITAN

class Model:
    def __init__(self, config):
        self.config = config
        self.loaded = False

    def load(self):
        self.loaded = True
        return True

    def is_loaded(self):
        return self.loaded

    def generate(self, token_ids, max_new_tokens=None):
        if not self.loaded:
            raise RuntimeError("النموذج غير محمّل.")

        limit = max_new_tokens or self.config.get(
            "max_new_tokens",
            512
        )

        return token_ids[:limit]

    def get_config(self):
        return self.config
