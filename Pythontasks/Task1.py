# Task 1: FizzBuzz Function
# Check if a number is divisible by both 3 and 5, return "FizzBuzz"
# Else if divisible by 3, return "Fizz"
# Else if divisible by 5, return "Buzz"
# Otherwise, print the number

def fizz_Buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_Buzz(5)
fizz_Buzz(30)

