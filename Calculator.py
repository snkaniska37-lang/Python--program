def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")

ch = int(input("Enter choice: "))

if ch == 1:
    print("Addition:", add(num1, num2))

elif ch == 2:
    print("Subtraction:", sub(num1, num2))

elif ch == 3:
    print("Multiplication:", mul(num1, num2))

elif ch == 4:
    print("Division:", div(num1, num2))

else:
    print("Invalid operator!")