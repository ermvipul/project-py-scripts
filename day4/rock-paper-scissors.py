import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Rock[0] wins against scissors[2]= 0>2.
# Scissors[2] win against paper[1]=2>1.
# Paper[1] wins against rock[0]=1>0.

map = [rock, paper, scissors]
print("Welcome to the Rock, paper, Scissors game!!!!!")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
random_choice = random.randint(0, 2)

if choice == 0 and random_choice ==2:
    print(map[choice])
    print(map[random_choice])
    print("You won")
elif choice ==1 and random_choice ==0:
    print(map[choice])
    print(map[random_choice])
    print("You won")
elif choice == 2 and random_choice == 1:
    print(map[choice])
    print(map[random_choice])
    print("You won")
elif choice == random_choice:
    print(map[choice])
    print(map[random_choice])
    print("its a draw")
else:
    print(map[choice])
    print(map[random_choice])
    print("You loose")