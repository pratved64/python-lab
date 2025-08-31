from functools import reduce

orders = [
    {"amount": 100, "completed": False},
    {"amount": 200, "completed": True},
    {"amount": 300, "completed": True},
    {"amount": 400, "completed": False}
]

# Filter orders by completed
completed = list(filter(lambda o: o['completed'], orders))

# Construct list of order amounts
amounts = list(map(lambda o: o['amount'], completed))

# Sum order amounts
total = reduce(lambda a, b: a + b, amounts)

print("Completed orders:")
print(*completed, sep="\n")
print("\nAmounts: ", end="")
print(*amounts, sep=", ")
print("\nTotal:", total)
