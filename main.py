expenses = []
budget = 0

while True:

    print("\n==============================")
    print("   EXPENSE MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Highest Expense")
    print("5. Category Summary")
    print("6. Set Monthly Budget")
    print("7. Check Budget")
    print("8. Search by Category")
    print("9. Expense Statistics")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\nAll Expenses:")

            for number, expense in enumerate(expenses, start=1):

                print(f"\nExpense {number}")
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])

    elif choice == "3":

        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("\nTotal Expense:", total)

    elif choice == "4":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            highest = expenses[0]

            for expense in expenses:
                if expense["amount"] > highest["amount"]:
                    highest = expense

            print("\nHighest Expense:")
            print("Amount:", highest["amount"])
            print("Category:", highest["category"])
            print("Description:", highest["description"])

    elif choice == "5":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            category_totals = {}

            for expense in expenses:

                category = expense["category"]
                amount = expense["amount"]

                if category in category_totals:
                    category_totals[category] = category_totals[category] + amount
                else:
                    category_totals[category] = amount

            print("\nCategory Summary:")

            for category, total in category_totals.items():
                print(category, ":", total)

    elif choice == "6":

        budget = float(input("Enter your monthly budget: "))

        print("Monthly budget set successfully!")

    elif choice == "7":

        if budget == 0:
            print("Please set your monthly budget first.")

        else:
            total = 0

            for expense in expenses:
                total = total + expense["amount"]

            remaining = budget - total

            print("\nMonthly Budget:", budget)
            print("Total Expense:", total)
            print("Remaining Budget:", remaining)

            if remaining > 0:
                print("You are within your budget.")

            elif remaining == 0:
                print("You have used your complete budget.")

            else:
                print("You have exceeded your budget.")

    elif choice == "8":

        search_category = input("Enter category to search: ")

        found = False

        for expense in expenses:

            if expense["category"].lower() == search_category.lower():

                print("\nAmount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])

                found = True

        if found == False:
            print("No expense found for this category.")

    elif choice == "9":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            total = 0
            highest = expenses[0]
            lowest = expenses[0]

            for expense in expenses:

                total = total + expense["amount"]

                if expense["amount"] > highest["amount"]:
                    highest = expense

                if expense["amount"] < lowest["amount"]:
                    lowest = expense

            average = total / len(expenses)

            print("\n========== EXPENSE STATISTICS ==========")
            print("Number of Expenses:", len(expenses))
            print("Total Expense:", total)
            print("Average Expense:", average)
            print("Highest Expense:", highest["amount"])
            print("Lowest Expense:", lowest["amount"])

    elif choice == "10":

        print("Thank you for using Expense Management System!")
        break

    else:

        print("Invalid choice. Please select 1-10.")