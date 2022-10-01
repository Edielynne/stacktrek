order = int(input("How many orders?\n"))

total = 0

for i in range (order):
    total += int(input(f"price {i+1} : "))
print(f"Total price:{total}")

