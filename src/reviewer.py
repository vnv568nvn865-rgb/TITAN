# مراجع TITAN

class Reviewer:
    def __init__(self, memory=None):
        self.memory = memory

    def review_requirements(self, requirements, completed):
        results = []

        for requirement in requirements:
            results.append({
                "requirement": requirement,
                "status": (
                    "completed"
                    if requirement in completed
                    else "incomplete"
                )
            })

        return results

    def review_tests(self, test_results):
        if not test_results:
            return {
                "status": "not_verified",
                "reason": "لم يتم تقديم نتائج اختبارات"
            }

        failed = [
            test for test in test_results
            if test.get("status") != "passed"
        ]

        return {
            "status": "passed" if not failed else "failed",
            "failed_tests": failed
        }

    def review(self, requirements=None, completed=None,
               test_results=None):
        requirements = requirements or []
        completed = completed or []

        requirement_results = self.review_requirements(
            requirements,
            completed
        )

        test_review = self.review_tests(
            test_results or []
        )

        requirements_ok = all(
            item["status"] == "completed"
            for item in requirement_results
        )

        tests_ok = test_review["status"] == "passed"

        if requirements_ok and tests_ok:
            status = "completed"
        else:
            status = "needs_review"

        result = {
            "status": status,
            "requirements": requirement_results,
            "tests": test_review
        }

        if self.memory:
            self.memory.add_short_term({
                "type": "review",
                "result": result
            })

        return result
