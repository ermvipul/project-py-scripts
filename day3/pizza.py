print("Welcome to py pizza Cal!")

size = input("What size of pizza do you want? S, M or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

#approach1
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill = bill + 2
    if extra_cheese == "Y":
        bill = bill + 1
    print(f"total bill is {bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1
    print(f"total bill is {bill}")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill = bill + 3
    if extra_cheese == "Y":
        bill = bill + 1
    print(f"total bill is {bill}")

# approach 2
prices = {"S": 15, "M": 20, "L": 25}
pepperoni_cost = {"S": 2, "M": 3, "L": 3}

bill = prices[size]
if add_pepperoni == "Y":
    bill += pepperoni_cost[size]
if extra_cheese == "Y":
    bill += 1

print(f"Total bill is {bill}")