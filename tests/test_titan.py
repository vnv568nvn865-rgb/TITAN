import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from titan import Titan


def test_titan_creation():
    titan = Titan()

    assert titan.memory is not None
    assert titan.planner is not None
    assert titan.executor is not None
    assert titan.tester is not None
    assert titan.diagnostic is not None
    assert titan.reviewer is not None


def test_titan_understand():
    titan = Titan()

    context = titan.understand(
        "احسب متوسط مجموعة من الأرقام"
    )

    assert context["goal"] == "احسب متوسط مجموعة من الأرقام"


def test_titan_plan():
    titan = Titan()

    titan.understand(
        "احسب متوسط مجموعة من الأرقام"
    )

    plan = titan.create_plan()

    assert "steps" in plan
    assert len(plan["steps"]) == 5


def test_titan_run():
    titan = Titan()

    result = titan.run(
        "اختبار نظام TITAN"
    )

    assert "context" in result
    assert "plan" in result
    assert "execution" in result
    assert "review" in result

    assert result["context"]["goal"] == "اختبار نظام TITAN"
    assert len(result["plan"]["steps"]) == 5
    assert len(result["execution"]) == 5


def test_titan_memory():
    titan = Titan()

    titan.run("اختبار الذاكرة")

    assert len(titan.memory.short_term) > 0
    assert len(titan.memory.long_term) > 0
