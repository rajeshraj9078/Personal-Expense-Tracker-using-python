from expenses import Expense
import calendar
import datetime

    
def main():
    print("👉 Running Expenses Tracker!")
    expense_file = "expenses_file.csv"
    budget = 200  
    
    # Get user input for expenses
    expense = get_user_expense()
    
    # Write their expense to a file
    save_expense_to_file(expense, expense_file)
    
    # Read file and summarize expenses
    read_file_summarize(expense_file, budget)  


def get_user_expense():
    print("Getting User Expenses")
    expense_name = input("👉 Enter expense name: ")

    
    while True:
        expense_amount = input("👉 Enter expense amount: ")
        try:
            expense_amount = float(expense_amount)  
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a numeric value.")

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "⛱️ Fun",
        "✅ Misu",
    ]
    
    while True:
        print("👉 Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        
        value_range = f"[1-{len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                break
            else:
                print("❌ Invalid selection. Please enter a number from", value_range)
        except ValueError:
            print("❌ Please enter a valid number.")

 
    return Expense(name=expense_name, category=selected_category, amount=expense_amount)

        
def save_expense_to_file(expense: Expense, expense_file):
    print(f"👉 Saving User Expense: {expense} to {expense_file}")
    with open(expense_file, "a", encoding="utf-8") as f:  
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

  
def read_file_summarize(expense_file, budget):
    print("👉 Summarizing User Expenses")

    expenses_list = []

    with open(expense_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")  
            print(expense_name, expense_category, expense_amount)

            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),  
                category=expense_category,
            )
            expenses_list.append(line_expense)

    
    amount_by_category = {}
    for expense in expenses_list:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount

    print("\n📈 Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    total_spent = sum(expense.amount for expense in expenses_list)
    print(f"\nYou've spent ${total_spent:.2f} this month.")

    remain_budget = budget - total_spent
    print(f"✅ Budget remaining: ${remain_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remain_days = days_in_month - now.day

    print("Remaining days in the current month:", remain_days)

    if remain_days > 0:
        daily_budget = remain_budget / remain_days
        print(f"👉 Budget per day: ${daily_budget:.2f}")
    else:
        print("⚠️ No days left in the month!")


if __name__ == "__main__":
    main()
