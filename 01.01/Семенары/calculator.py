class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: float, category: str):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.expenses.append({"amount": amount, "category": category})

    def total_expenses(self) -> float:
        return sum(e["amount"] for e in self.expenses)

    def expenses_by_category(self, category: str) -> list:
        return [e for e in self.expenses if e["category"] == category]