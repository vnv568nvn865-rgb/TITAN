# محرك تنفيذ TITAN

class Executor:
    def __init__(self, memory=None):
        self.memory = memory
        self.results = []

    def execute_step(self, step):
        result = {
            "step": step,
            "status": "completed",
            "result": None,
            "error": None
        }

        self.results.append(result)

        if self.memory:
            self.memory.add_short_term({
                "type": "execution",
                "result": result
            })

        return result

    def execute_plan(self, plan):
        results = []

        for step in plan.get("steps", []):
            result = self.execute_step(step)
            results.append(result)

        return results

    def get_results(self):
        return self.results

    def clear_results(self):
        self.results.clear()
