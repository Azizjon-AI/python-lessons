def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return "Неизвестная операция!"

a = int(input("вывестите число: a = "))
b = int(input("вывестите число: b = "))
operation = input("что хотите делат: '+', '-', '*', '/': ")
print(calculate(a, b, operation))