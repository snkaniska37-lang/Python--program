def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter a fibonacci limit: "))

if n <= 0:
    print("Not possible")
else:
    print(f"First {n} Fibonacci numbers:")

    for i in range(n):
        print(fibonacci(i), end=" ")