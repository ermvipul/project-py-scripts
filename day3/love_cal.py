print("Welcome to the love cal!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()
com_string = name1 + name2

t1 = name1.count("t")
t2 = name1.count("r")
t3 = name1.count("u")
t4 = name1.count("e")
l1 = name1.count("t")
l2 = name1.count("r")
l3 = name1.count("u")
l4 = name1.count("e")


total_name1 = t1 + t2 + t3 + t4
total_name2 = l1 + l2 + l3 + l4

total = str(total_name1) + str(total_name2)

total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke & mentos")
elif 40 <= total <= 50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")