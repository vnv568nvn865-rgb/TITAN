# مخطط مهام TITAN

class Planner:
    def __init__(self, memory=None):
        self.memory = memory

    def create_plan(self, context):
        goal = context.get("goal", "")

        plan = [
            {
                "step": 1,
                "action": "فهم المهمة",
                "status": "pending"
            },
            {
                "step": 2,
                "action": "جمع السياق المطلوب",
                "status": "pending"
            },
            {
                "step": 3,
                "action": "تنفيذ الحل",
                "status": "pending"
            },
            {
                "step": 4,
                "action": "اختبار النتيجة",
                "status": "pending"
            },
            {
                "step": 5,
                "action": "مراجعة العمل",
                "status": "pending"
            }
        ]

        result = {
            "goal": goal,
            "steps": plan
        }

        if self.memory:
            self.memory.add_short_term({
                "type": "planner",
                "plan": result
            })

        return result

    def update_plan(self, plan, failure):
        for step in plan["steps"]:
            if step["status"] == "pending":
                step["status"] = "needs_review"
                break

        if self.memory:
            self.memory.add_short_term({
                "type": "plan_update",
                "failure": failure,
                "plan": plan
            })

        return plan

    def complete_step(self, plan, step_number):
        for step in plan["steps"]:
            if step["step"] == step_number:
                step["status"] = "completed"
                break

        return plan
