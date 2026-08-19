# واجهة نموذج TITAN
#
# هذه الطبقة لا تحتوي على محرك الاستدلال نفسه.
# المحرك الفعلي سيتم ربطه لاحقًا عبر backend.

class Model:
    def __init__(self, config, backend=None):
        self.config = config
        self.backend = backend
        self.loaded = False

    def load(self):
        if self.backend is None:
            raise RuntimeError(
                "لم يتم ربط محرك النموذج بعد."
            )

        self.backend.load(self.config)
        self.loaded = True

        return True

    def is_loaded(self):
        return self.loaded

    def generate(self, token_ids, max_new_tokens=None):
        if not self.loaded:
            raise RuntimeError(
                "النموذج غير محمّل."
            )

        return self.backend.generate(
            token_ids,
            max_new_tokens=max_new_tokens
        )

    def get_config(self):
        return self.config

    def get_backend(self):
        return self.backend
