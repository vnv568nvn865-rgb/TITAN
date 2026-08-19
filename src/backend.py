# واجهة محرك الاستدلال في TITAN

class Backend:
    def __init__(self):
        self.loaded = False

    def load(self, config):
        raise NotImplementedError(
            "يجب تنفيذ محرك الاستدلال الفعلي."
        )

    def generate(self, token_ids, max_new_tokens=None):
        raise NotImplementedError(
            "يجب تنفيذ generate في محرك الاستدلال."
        )

    def is_loaded(self):
        return self.loaded
