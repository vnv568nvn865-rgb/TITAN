# ذاكرة TITAN

class Memory:
    def __init__(self):
        self.short_term = []
        self.project_memory = []
        self.long_term = []

    def add_short_term(self, item):
        self.short_term.append(item)

    def add_project_memory(self, item):
        self.project_memory.append(item)

    def add_long_term(self, item):
        self.long_term.append(item)

    def get_short_term(self):
        return self.short_term

    def get_project_memory(self):
        return self.project_memory

    def get_long_term(self):
        return self.long_term

    def remember(self, item, memory_type="short_term"):
        if memory_type == "project":
            self.add_project_memory(item)
        elif memory_type == "long_term":
            self.add_long_term(item)
        else:
            self.add_short_term(item)

    def clear_short_term(self):
        self.short_term.clear()
