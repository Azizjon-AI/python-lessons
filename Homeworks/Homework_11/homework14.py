try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Вебиреите оператцию: +, -, *, /: ")
    if operation == "+":
        print(f"{a} + {b} = {a + b}")
    elif operation == "-":
        print(f"{a} - {b} = {a - b}")
    elif operation == "*":
        print(f"{a} * {b} = {a * b}")
    elif operation == "/":
        print(f"{a} / {b} = {a / b}")
except ValueError:
    print("Введите число не текст")
except ZeroDivisionError:
    print("Деление на нол невазможно")
except Exception as e:
    print(f"Неизвестная операция {e}")
finally:
    print("Программа завершина")