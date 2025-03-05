import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define categories globally so it's accessible everywhere
categories = {
    'food': ['restaurant', 'grocery', 'coffee', 'dinner', 'lunch'],
    'transport': ['gas', 'bus', 'train', 'uber', 'taxi', 'flight'],
    'entertainment': ['movie', 'game', 'concert', 'netflix', 'party'],
    'bills': ['rent', 'electricity', 'phone', 'internet', 'water'],
    'health': ['doctor', 'pharmacy', 'gym', 'insurance'],
    'shopping': ['clothes', 'electronics', 'amazon', 'gift'],
    'education': ['books', 'course', 'tuition', 'school'],
    'travel': ['hotel', 'airbnb', 'trip', 'vacation']
}

def categorize_expense(amount, description, user_category=None):
    """Categorize an expense based on description and amount, or use user-provided category."""
    if user_category and user_category.lower() != "auto":
        return user_category.lower()

    # Use the globally defined categories dictionary
    description = description.lower()
    for category, keywords in categories.items():
        if any(keyword in description for keyword in keywords):
            return category
    return 'miscellaneous'

def calculate_balance(transactions):
    """Calculate total balance from a list of transactions."""
    return sum(amount for amount, _, _, _ in transactions)

def generate_summary(transactions):
    """Generate a summary of transactions by category."""
    summary = {}
    for amount, description, _, category in transactions:
        summary[category] = summary.get(category, 0) + amount
    return summary

def main():
    """Main function to run the Streamlit finance tracker."""
    st.title("Personal Finance Tracker")
    
    # Initialize session state for transactions and budget
    if 'transactions' not in st.session_state:
        st.session_state.transactions = []
    if 'monthly_budget' not in st.session_state:
        st.session_state.monthly_budget = 0.0

    # Sidebar for budget setting
    with st.sidebar:
        st.header("Budget Settings")
        budget = st.number_input("Set Monthly Budget", min_value=0.0, value=st.session_state.monthly_budget)
        if st.button("Update Budget"):
            st.session_state.monthly_budget = budget
        st.write(f"Current Monthly Budget: ${st.session_state.monthly_budget:.2f}")

    # Transaction input
    st.header("Add Transaction")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        trans_type = st.selectbox("Type", ["Income", "Expense"])
    with col2:
        amount = st.number_input("Amount", min_value=0.0)
    with col3:
        description = st.text_input("Description")
    with col4:
        # Use the globally defined categories dictionary directly
        categories_list = list(globals()['categories'].keys()) + ["Miscellaneous", "Auto"]
        category = st.selectbox("Category (or 'Auto' for automatic)", categories_list, index=len(categories_list)-1)
    
    if st.button("Add Transaction"):
        if description and amount > 0:
            final_amount = amount if trans_type == "Income" else -amount
            date = datetime.now().strftime("%Y-%m-%d")
            st.session_state.transactions.append((final_amount, description, date, category))
            st.success("Transaction added!")

    # Display transactions and summary
    if st.session_state.transactions:
        df = pd.DataFrame(st.session_state.transactions, columns=['Amount', 'Description', 'Date', 'Category'])
        
        # Summary
        st.header("Financial Summary")
        balance = calculate_balance(st.session_state.transactions)
        summary = generate_summary(st.session_state.transactions)
        
        st.write(f"Total Balance: ${balance:.2f}")
        budget_status = balance - st.session_state.monthly_budget if balance < 0 else st.session_state.monthly_budget - (-balance)
        st.write(f"Budget Remaining: ${budget_status:.2f}")
        if balance < 0 and -balance > st.session_state.monthly_budget:
            st.warning("You've exceeded your monthly budget!")
        
        # Category breakdown
        st.subheader("Category Breakdown")
        st.dataframe(pd.DataFrame.from_dict(summary, orient='index', columns=['Total']).sort_values(by='Total'))

        # Visualization
        st.subheader("Spending Visualization")
        fig, ax = plt.subplots()
        categories = list(summary.keys())
        amounts = [abs(v) if v < 0 else 0 for v in summary.values()]  # Show only expenses

        if any(amount > 0 for amount in amounts):  # Check if there are any expenses to visualize
            ax.pie(amounts, labels=categories, autopct='%1.1f%%')
            ax.axis('equal')
        else:
            st.write("No expenses to visualize. Add expense transactions to see a spending breakdown.")

        st.pyplot(fig)

        # Transaction history
        st.subheader("Transaction History")
        st.dataframe(df)
    else:
        st.write("No transactions recorded. Add transactions to see a summary and visualization.")

if __name__ == "__main__":
    main()