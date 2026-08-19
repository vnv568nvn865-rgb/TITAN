from memory import Memory
from planner import Planner
from executor import Executor
from tester import Tester
from diagnostic import Diagnostic
from reviewer import Reviewer
from model import Model
from tokenizer import Tokenizer
from model_config import get_model_config


class Titan:
    def __init__(self):
        self.memory = Memory()
        self.planner = Planner(self.memory)
        self.executor = Executor(self.memory)
        self.tester = Tester(self.memory)
        self.diagnostic = Diagnostic(self.memory)
        self.reviewer = Reviewer(self.memory)

        self.config = get_model_config()
        self.tokenizer = Tokenizer()
        self.model = Model(self.config)

        self.current_task = None
        self.context = None
        self.plan = None

    def load_model(self):
        return self.model.load()

    def understand(self, task):
        self.current_task = task

        self.context = {
            "goal": task,
            "requirements": [],
            "constraints": [],
            "missing_information": []
        }

        self.memory.add_short_term({
            "type": "understanding",
            "context": self.context
        })

        return self.context

    def create_plan(self):
        if self.context is None:
            raise ValueError("يجب فهم المهمة أولًا")

        self.plan = self.planner.create_plan(
            self.context
        )

        return self.plan

    def generate(self, prompt):
        if not self.model.is_loaded():
            self.load_model()

        token_ids = self.tokenizer.encode(prompt)

        output_ids = self.model.generate(
            token_ids,
            self.config["max_new_tokens"]
        )

        return self.tokenizer.decode(output_ids)

    def execute(self):
        if self.plan is None:
            raise ValueError("يجب إنشاء خطة أولًا")

        return self.executor.execute_plan(
            self.plan
        )

    def test(self, function, expected, *args, **kwargs):
        return self.tester.run_test(
            "اختبار الوظيفة",
            function,
            expected,
            *args,
            **kwargs
        )

    def diagnose(self, error, context=None):
        return self.diagnostic.analyze(
            error,
            context
        )

    def review(self, requirements=None, completed=None):
        return self.reviewer.review(
            requirements=requirements or [],
            completed=completed or [],
            test_results=self.tester.get_results()
        )

    def remember(self, experience):
        self.memory.remember(
            experience,
            memory_type="long_term"
        )

    def run(self, task):
        self.understand(task)

        plan = self.create_plan()

        execution_results = self.execute()

        review = self.review()

        experience = {
            "task": task,
            "plan": plan,
            "execution": execution_results,
            "review": review
        }

        self.remember(experience)

        return {
            "context": self.context,
            "plan": plan,
            "execution": execution_results,
            "review": review
        }


if __name__ == "__main__":
    titan = Titan()

    titan.load_model()

    print("=== TITAN ===")
    print("النموذج:", titan.config["name"])
    print("المعاملات:", titan.config["parameters"])

    result = titan.run(
        "اختبار نظام TITAN"
    )

    print("\n=== الخطة ===")

    for step in result["plan"]["steps"]:
        print(
            step["step"],
            "-",
            step["action"]
        )

    print("\n=== اختبار النموذج ===")

    response = titan.generate(
        "اكتب خطة بسيطة لإصلاح خطأ برمجي"
    )

    print(response)

    print("\n=== المراجعة ===")
    print(result["review"])
