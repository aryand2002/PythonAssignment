def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x,end=" ")
        x = y
        y = x + y

fibonacci(10)
fibonacci(8)