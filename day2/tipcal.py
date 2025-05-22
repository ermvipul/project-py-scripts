# add a greeting for the user
print("Welcome to the tip calculator!")

# ask for the total amount
bill = float(input("what was the total bill? "))

# ask for the %age of tip user would like to pay(10, 12 or 15)
tip = float(input("What % age of tip would you like to give? 10, 12, or 15 "))
actual_tip = bill * (tip/100)
# number of people that will split the bill
persons = int(input("How many people will split the bill? "))

# show the actual result
share = "{:.2f}".format(round(((bill + actual_tip) / persons),2))
print(f"Each person should pay: {share}")