# نظام تشخيص الأخطاء في TITAN

class Diagnostic:
    def __init__(self, memory=None):
        self.memory = memory
        self.diagnoses = []

    def analyze(self, error, context=None):
        diagnosis = {
            "error": str(error),
            "context": context or {},
            "cause": None,
            "solution": None,
            "status": "needs_analysis"
        }

        self.diagnoses.append(diagnosis)

        if self.memory:
            self.memory.add_short_term({
                "type": "diagnostic",
                "result": diagnosis
            })

        return diagnosis

    def set_cause(self, diagnosis, cause):
        diagnosis["cause"] = cause
        return diagnosis

    def set_solution(self, diagnosis, solution):
        diagnosis["solution"] = solution
        return diagnosis

    def mark_resolved(self, diagnosis):
        diagnosis["status"] = "resolved"

        if self.memory:
            self.memory.add_short_term({
                "type": "diagnostic_resolved",
                "result": diagnosis
            })

        return diagnosis

    def get_diagnoses(self):
        return self.diagnoses

    def clear(self):
        self.diagnoses.clear()
