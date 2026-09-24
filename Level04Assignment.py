#Expense entry loop
expenses = []

while True:
    try:
        entry = float(input("Enter an expense or 0 to finish: "))
    except ValueError:
        print("Please enter a number, not words.")
        continue

    if entry == 0:
        print()
        break

    elif entry < 0:
        print("Please enter a positive number.")

    else:
        expenses.append(entry)

#If statements for what to classify the expense as

small_expenses = []
moderate_expenses = []
large_expenses = []

for expense in expenses:
    if expense < 25:
        small_expenses.append(expense)
    elif expense <= 100:
        moderate_expenses.append(expense)
    else:
        large_expenses.append(expense)


#Printing results 
print("Expense Summary")
total = sum(expenses)
average = total / len(expenses)

print("Number of expenses:", len(expenses))
print("Total amount: $" + format(total, ",.2f"))
print("Average expense: $" + format(average, ",.2f"))
print("Smallest expense: $" + format(min(expenses), ",.2f"))
print("Largest expense: $" + format(max(expenses), ",.2f"))
print()
print("Small expenses:", len(small_expenses))
print("Moderate expenses:", len(moderate_expenses))
print("Large expenses:", len(large_expenses))
