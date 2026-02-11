# Simple Bookkeeping Tool by DataWithMayLauren

def calculate_expenses():
    print("--- May Lauren's Expense Tracker ---")
    
    # Asking the user for input
    income = float(input("Enter total monthly income: "))
    expenses = float(input("Enter total monthly expenses: "))
    
    # The math (Python handles the logic)
    profit = income - expenses
    savings_rate = (profit / income) * 100
    
    # Displaying the results
    print(f"\nResults for this month:")
    print(f"Net Profit: ${profit:.2f}")
    print(f"Savings Rate: {savings_rate:.2f}%")

# Running the function
calculate_expenses()
