import random

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', '\'', '<', '>', ',', '.', '?', '/','`', '~'
]

print("Welcome to password generator!!!")
nr_letters = int(input("How many letters you will like in your password?\n"))
nr_numbers = int(input("How many numbers you will like in your password?\n"))
nr_symbols = int(input("How many symbols you will like in your password?\n"))

# Adding letters to the list
nrl = []
for _ in range(nr_letters):
    letter = random.choice(alphabets)
    nrl.append(letter)
print("Letters:", nrl)

# Adding numbers to the list
for _ in range(nr_numbers):
    number = random.choice(numbers)
    nrl.append(number)
print("Numbers Added:", nrl)

# Adding symbols to the list
for _ in range(nr_symbols):
    symbol = random.choice(symbols)
    nrl.append(symbol)
print("Symbols Added:", nrl)

# Final randomized password
random.shuffle(nrl)
print("Generated Password:", ''.join(nrl))
