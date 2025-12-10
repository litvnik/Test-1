import pytest
from calculator import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_add_expense_positive(tracker):
    tracker.add_expense(100.0, "food")
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0]["amount"] == 100.0

def test_add_expense_negative_raises_error(tracker):
    with pytest.raises(ValueError):
        tracker.add_expense(-50, "gift")

def test_total_expenses(tracker):
    tracker.add_expense(30.0, "transport")
    tracker.add_expense(70.0, "food")
    assert tracker.total_expenses() == 100.0

@pytest.mark.parametrize("amount,category", [
    (25.5, "entertainment"),
    (100, "utilities"),
    (0.99, "snacks")
])
def test_parametrized_expenses(tracker, amount, category):
    tracker.add_expense(amount, category)
    assert tracker.expenses_by_category(category)[0]["amount"] == amount