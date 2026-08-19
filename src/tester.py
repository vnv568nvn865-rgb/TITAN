# محرك اختبار TITAN

class Tester:
    def __init__(self, memory=None):
        self.memory = memory
        self.tests = []

    def add_test(self, name, expected, actual):
        test = {
            "name": name,
            "expected": expected,
            "actual": actual,
            "status": "passed" if expected == actual else "failed"
        }

        self.tests.append(test)

        if self.memory:
            self.memory.add_short_term({
                "type": "test",
                "result": test
            })

        return test

    def run_test(self, name, function, expected, *args, **kwargs):
        try:
            actual = function(*args, **kwargs)
            return self.add_test(name, expected, actual)
        except Exception as error:
            test = {
                "name": name,
                "expected": expected,
                "actual": None,
                "status": "failed",
                "error": str(error)
            }

            self.tests.append(test)

            if self.memory:
                self.memory.add_short_term({
                    "type": "test",
                    "result": test
                })

            return test

    def all_passed(self):
        return all(
            test["status"] == "passed"
            for test in self.tests
        )

    def get_results(self):
        return self.tests

    def clear(self):
        self.tests.clear()
