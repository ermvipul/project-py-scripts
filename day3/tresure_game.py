print("Welcome to tresure island!!!!")
print("Your mission is to find tresure.")

first = input("Choose a direction - left or right?").lower()

if first == "right":
    print("game over")
elif first == "left":
    second = input("Now you are at the river, you wanna wait for the boat or swim across? 'Swim' or 'Wait'")
    if second == "wait":
        third = input("Choose a color - 'Red', 'Blue', 'Yellow'")
        if third == "yellow":
            print("You won")
        else:
            print("Game over")
    else:
        print("game over")