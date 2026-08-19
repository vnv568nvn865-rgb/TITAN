class Titan:
    def __init__(self):
        self.memory = []
        self.current_task = None

    def understand(self, task):
        self.current_task = task
        return {
            "goal": task,
            "requirements": [],
            "constraints": [],
            "missing_information": []
        }

    def plan(self, context):
        return [
            "فهم المهمة",
            "جمع السياق",
            "تنفيذ الحل",
            "اختبار النتيجة",
            "مراجعة العمل"
        ]

    def execute(self, step):
        return {
            "step": step,
            "status": "pending",
            "result": None
        }

    def remember(self, experience):
        self.memory.append(experience)

    def run(self, task):
        context = self.understand(task)
        plan = self.plan(context)

        results = []

        for step in plan:
            result = self.execute(step)
            results.append(result)

        self.remember({
            "task": task,
            "plan": plan,
            "results": results
        })

        return results


if __name__ == "__main__":
    titan = Titan()

    result = titan.run(
        "حلل المهمة وأنشئ خطة لتنفيذها"
    )

    for item in result:
        print(item)
