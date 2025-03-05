import pytest
from project import categorize_expense, calculate_balance, generate_summary

def test_categorize_expense():
    assert categorize_expense(10.50, "grocery shopping") == "food"
    assert categorize_expense(25.00, "uber ride") == "transport"
    assert categorize_expense(15.75, "phone bill") == "bills"
    assert categorize_expense(30.00, "doctor visit") == "health"
    assert categorize_expense(50.00, "amazon purchase") == "shopping"
    assert categorize_expense(5.00, "random stuff") == "miscellaneous"
    assert categorize_expense(10.00, "random stuff", "food") == "food"  # Test user category

def test_calculate_balance():
    transactions = [(100.0, "salary", "2025-03-01", "income"), (-50.0, "rent", "2025-03-02", "bills"), (25.0, "bonus", "2025-03-03", "income")]
    assert calculate_balance(transactions) == 75.0
    assert calculate_balance([]) == 0.0
    assert calculate_balance([(-10.0, "food", "2025-03-01", "food")]) == -10.0

def test_generate_summary():
    transactions = [
        (100.0, "grocery shopping", "2025-03-01", "food"),
        (-50.0, "uber ride", "2025-03-02", "transport"),
        (-25.0, "phone bill", "2025-03-03", "bills")
    ]
    summary = generate_summary(transactions)
    assert summary["food"] == 100.0
    assert summary["transport"] == -50.0
    assert summary["bills"] == -25.0