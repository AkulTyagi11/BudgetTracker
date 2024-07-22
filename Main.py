class Transaction:
    def __init__(self):
        self.income = 0.0
        self.expense = 0.0
        self.category = ""

class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
        self.income = 0.0
        self.categories = [0.0, 0.0, 0.0, 0.0] # Food, Utilities, Entertainment, Other
        self.transactions = [Transaction() for _ in range(100)]
        self.transaction_count = 0
        self.income_entered = False # Flag to track if income has been entered

def initialize(tracker):
    tracker.balance = 0
    tracker.income = 0
    tracker.income_entered = False
    for i in range(4):
        tracker.categories[i] = 0
    tracker.transaction_count = 0

def add_transaction(tracker):
    transaction = Transaction()
    # Check if income has already been entered
    if not tracker.income_entered:
        tracker.income = float(input("Enter Income: "))
        tracker.income_entered = True # Set the flag to indicate income has been entered
    transaction.expense = float(input("Enter Expense: "))
    print("Choose category:")
    print("1. Food")
    print("2. Utilities")
    print("3. Entertainment")
    print("4. Other")
    category_choice = int(input("Enter your Choice: "))
    if category_choice == 1:
        transaction.category = "Food"
    elif category_choice == 2:
        transaction.category = "Utilities"
    elif category_choice == 3:
        transaction.category = "Entertainment"
    elif category_choice == 4:
        transaction.category = "Other"
    else:
        print("Invalid category choice. Using 'other'.")
        transaction.category = "other"

    if transaction.category == "Food":
        tracker.categories[0] += transaction.expense
    elif transaction.category == "Utilities":
        tracker.categories[1] += transaction.expense
    elif transaction.category == "Entertainment":
        tracker.categories[2] += transaction.expense
    else:
        tracker.categories[3] += transaction.expense

    tracker.balance = tracker.income - sum(tracker.categories)
    tracker.transactions[tracker.transaction_count] = transaction
    tracker.transaction_count += 1
    print("Transaction added successfully!")

def show_transactions(tracker):
    if tracker.transaction_count == 0:
        print("No transactions to display.")
    else:
        print("Transactions:")
        for i in range(tracker.transaction_count):
            print(f"Income: {tracker.income}, Expense: {tracker.transactions[i].expense}, Category: {tracker.transactions[i].category}")

def show_summary(tracker):
    print("Expense Summary by Category:")
    print(f"Food: {tracker.categories[0]:.2f}")
    print(f"Utilities: {tracker.categories[1]:.2f}")
    print(f"Entertainment: {tracker.categories[2]:.2f}")
    print(f"Other: {tracker.categories[3]:.2f}")
    total_expense = sum(tracker.categories)
    remaining_balance = tracker.income - total_expense
    print(f"Total Amount Spent: {total_expense:.2f}")
    print(f"Remaining Balance: {remaining_balance:.2f}")

if __name__ == "__main__":
    tracker = BudgetTracker()
    initialize(tracker)
    while True:
        print("\n1. Add Transaction\n2. Show Transactions\n3. Show Summary\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_transaction(tracker)
        elif choice == 2:
            show_transactions(tracker)
        elif choice == 3:
            show_summary(tracker)
        elif choice == 4:
            print("Thank you for entering your expenditures. Spend wisely!")
            break
        else:
            print("Invalid choice. Please try again.")