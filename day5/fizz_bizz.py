for num in range(1,101):
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 5 ==0 and num % 3==0:
        print("FizzBuzz")
    else:
        print(num)