print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("Can ride")
    age = int(input("Enter age: "))
    bill = 0
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif 55 >= age <= 45 :
        bill = 0
    else:
        bill = 12
    wants_photo = input("Do you want a photo? Y or N")
    if wants_photo == "Y":
        bill = bill + 1
    else:
        bill = bill
    print(f"Total bill is ${bill}")
else:
    print("can't ride")