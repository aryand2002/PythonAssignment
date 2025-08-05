# Task: Fibonacci Series Generator
# Prints the first 'n' numbers in the Fibonacci sequence

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # For newline after the sequence

fibonacci(10)
fibonacci(8)
