# Automated Bookkeeping Tool by DataWithMayLauren
import sys

def calculate_expenses(income, expenses):
    profit = income - expenses
    savings_rate = (profit / income) * 100 if income > 0 else 0
    
    print(f"--- Financial Summary ---")
    print(f"Total Income:  ${income:,.2f}")
    print(f"Total Expense: ${expenses:,.2f}")
    print(f"Net Profit:    ${profit:,.2f}")
    print(f"Savings Rate:  {savings_rate:.2f}%")

if __name__ == "__main__":
    # If a human is running it, ask for input. 
    # If GitHub is running it, use these test numbers.
    try:
        if sys.stdin.isatty():
            inc = float(input("Enter income: "))
            exp = float(input("Enter expenses: "))
        else:
            inc, exp = 5000.0, 3200.0 # Standard test numbers
        
        calculate_expenses(inc, exp)
    except Exception as e:
        print(f"Error: {e}")
