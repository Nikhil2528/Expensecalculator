import json
from datetime import datetime, timedelta

   
def save_expense(date, expense):
    try:
        with open('expenses.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        # Handle the case where the file is empty or contains invalid JSON
        data = {}        

    if date in data:
        data[date].append(expense)
    else:
        data[date] = [expense]
    with open('expenses.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Expense saved successfully.")
    check_budget()

def edit_expense(date, new_expense):
    with open('expenses.json', 'r') as file:
        data = json.load(file)
    if date in data:
        old_expense = float(input("Enter the old expense amount: $"))
        if old_expense in data[date]:
            index = data[date].index(old_expense)
            data[date][index] = new_expense
            with open('expenses.json', 'w') as file:
                json.dump(data, file, indent=4)
        
            print("Expense edited successfully.")
            
        else:
            print("Expense not found for the given date.")
    else:
        print("No expenses found for the given date.")

def check_budget():
    today = datetime.now().date()
    fourteen_days_ago = today - timedelta(days=14)
    total_expenses = 0
    days_expenses = 0
    with open('expenses.json', 'r') as file:
        data = json.load(file)
    for date, expenses in data.items():
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        if fourteen_days_ago <= date_obj <= today:
            total_expenses += sum(expenses)
            days_expenses += 1
    budget = 1000
    fifty_percent_budget = budget * 0.5
    remaining_days = 14 - days_expenses
    remaining_budget = budget - total_expenses
    budget_per_day = remaining_budget / remaining_days
    if days_expenses == 14 and total_expenses >= fifty_percent_budget:
        print(f"Warning: You have used 50% of your budget after 14 days.")
    elif days_expenses > 14:
        print(f"Warning: You have exceeded 14 days of expenses.")
    elif total_expenses > budget:
        print(f"Warning: Total expenses for the last 14 days (${total_expenses}) exceed the budget (${budget}).")
    else:
        print(f"Remaining budget for the next {remaining_days} days: ${remaining_budget}")
        print(f"Budget per day for the remaining period: ${budget_per_day:.2f}")
    return total_expenses
    

def main(edit_or_add):
    if edit_or_add == 'edit':
        edit_date = input("Enter the date of the expense to edit (YYYY-MM-DD): ")
        new_expense = float(input("Enter the new expense amount: $"))
        edit_expense(edit_date, new_expense)  # Pass only date and new_expense arguments
    elif edit_or_add == 'add':
        date = input("Enter the date (YYYY-MM-DD): ")
        expense = float(input("Enter the expense for the day: $"))
        save_expense(date, expense)
    else:
        print("Invalid option.")
   

if __name__ == "__main__":
    option = input("Do you want to edit an expense or add a new one? (edit/add): ").lower()
    main(option)
