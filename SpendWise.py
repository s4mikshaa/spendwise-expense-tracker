expenses = []

while True:
    print("\nSPENDWISE EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Expense is added successfully!")

    elif choice == "2":
        print("\nYOUR EXPENSES")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            total = 0

            for expense in expenses:
                print(
                    expense["category"],
                    "- ₹", expense["amount"],
                    "-",
                    expense["description"]
                )

                total += expense["amount"]

            print("\nTotal Spent: ₹", total)

    elif choice == "3":
        print("Thank you for using SpendWise!")
        break

    else:
        print("Invalid choice!! Please try again.")