height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round((weight / (height ** 2)), 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are Underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You are Normal weight")
elif 30 > bmi:
    print(f"Your bmi is {bmi}, You are Overweight")
elif 35 > bmi:
    print(f"Your bmi is {bmi}, You are Obsese")
else:
    print(f"Your bmi is {bmi}, You are Clinically obese")