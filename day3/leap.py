# year / 4
# year !/ 100
# year / 400

year = int(input("Which year you want to check? "))

# year / 4 but not by 100 but by 400

## approach 1
if year % 4 == 0:
    print("1")
    if year % 100 != 0 or year % 400 == 0:
        print("Leap yr")
else:
    print("Not Leap yr")

## approach2
if year % 4 == 0:
    if year % 100 == 0: 
        if year % 400 == 0:
            print("Leap yr")
        else:
            print("Not Leap yr")
    else:
        print("not Leap yr")
else:
    print("not Leap yr")