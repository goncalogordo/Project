def categorize_expense(amount, description):
    """Categorize an expense based on description and amount."""
    categories = {
        'food': ['restaurant', 'grocery', 'coffee'],
        'transport': ['gas', 'bus', 'train', 'uber'],
        'entertainment': ['movie', 'game', 'concert'],
        'bills': ['rent', 'electricity', 'phone'],
    }
    
    description = description.lower()
    for category, keywords in categories.items():
        if any(keyword in description for keyword in keywords):
            return category
    return 'miscellaneous'

def calculate_balance(transactions):
    """Calculate total balance from a list of transactions."""
    return sum(amount for amount, _ in transactions)

def generate_summary(transactions):
    """Generate a summary of transactions by category."""
    summary = {}
    for amount, description in transactions:
        category = categorize_expense(amount, description)
        summary[category] = summary.get(category, 0) + amount
    return summary

def main():
    """Main function to run the personal finance tracker."""
    transactions = []
    
    print("Welcome to Personal Finance Tracker!")
    print("Enter 'q' to quit and see summary")
    
    while True:
        action = input("Add (I)ncome or (E)xpense? (q to quit): ").lower()
        
        if action == 'q':
            break
        elif action not in ['i', 'e']:
            print("Invalid input. Please use 'i', 'e', or 'q'")
            continue
            
        try:
            amount = float(input("Enter amount: "))
            if action == 'e':
                amount = -amount  # Expenses are negative
            description = input("Enter description: ")
            transactions.append((amount, description))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
    
    if transactions:
        balance = calculate_balance(transactions)
        summary = generate_summary(transactions)
        
        print("\n=== Finance Summary ===")
        print(f"Total Balance: ${balance:.2f}")
        print("\nBreakdown by Category:")
        for category, total in summary.items():
            print(f"{category.capitalize():15} ${total:.2f}")
    else:
        print("\nNo transactions recorded.")

if __name__ == "__main__":
    main()