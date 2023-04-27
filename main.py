# Write your code heref
print("Earned amount:")
income = 0.0


def main(x, y):
    global income
    print(f"{x}: ${y}")
    income += float(y)


for i, j in (("Bubblegum", 202), ("Toffee", 118), ("Ice cream", 2250), ("Milk chocolate", 1680), ("Doughnut", 1075), ("Pancake", 80)):
    main(i, j)

print()
print(f"Income: ${income}")

staff_expenses = input("Staff expenses:")
other_expenses = input("Other expenses:")

print(f"Net income: ${income - int(staff_expenses) - int(other_expenses)}")
