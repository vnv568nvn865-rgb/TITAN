from memory import Memory


class Titan:
    def __init__(self):
        self.memory = Memory()
        self.current_task = None

    def understand(self, task):
        self.current_task = task

        context = {
            "goal": task,
            "requirements": [],
            "constraints": [],
            "missing_information": []
        }

        self.memory.add_short_term({
            "type": "understanding",
            "context": context
        })

        return context

    def plan(self, context):
        plan = [
            "فهم المهمة",
            "جمع السياق",
            "تنفيذ الحل",
            "اختبار النتيجة",
            "مراجعة العمل"
        ]

        self.memory.add_short_term({
            "type": "plan",
            "steps": plan
        })

        return plan

    def execute(self, step):
        result = {
            "step": step,
            "status": "pending",
            "result": None
        }

        self.memory.add_short_term({
            "type": "execution",
            "result": result
        })

        return result

    def remember(self, experience):
        self.memory.remember(
            experience,
            memory_type="long_term"
        )

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
