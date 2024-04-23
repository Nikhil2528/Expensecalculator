import json
import sys

# new_expenses = sys.argv # this is a string



with open('expense_tracker.json') as f:
    existing_expenses = json.load(f)

    print(existing_expenses)

print(new_expenses)

final_expenses = existing_expenses.append(dict(new_expenses))

print(final_expenses)

# # Convert dictionary to JSON string
# with open('expense_tracker.json', 'w') as fp:
#     json.dump(final_expenses, fp)new_expenses=eval(sys.argv[1])