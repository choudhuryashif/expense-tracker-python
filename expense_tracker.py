expenses=[]
while True:
    print("\-----Expenses Tracker Menu-----")
    print("1. Add Expense" )
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choose=input("Select your option (1-4):")

    if choose == "1":
        add_expense=int(input("Enter expense : "))
        expenses.append(add_expense)
    elif choose == "2":
        for i, expense in enumerate(expenses, start=1):
         print(i, ".", expense)
    elif choose == "3":
       print(sum(expenses))
    elif choose == "4":
        print("👋 Goodby! Thanks for using expenses tracker ")
        break
    else:
       print("❌ Oops! Invalid choice. Please enter 1, 2, 3 or 4")
