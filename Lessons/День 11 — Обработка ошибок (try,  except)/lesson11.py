# try:
    # код который может вызвать ошибку
# except ТипОшибки:
    # что делать если ошибка произошла
 

try:
    age = int(input("Введи возраст: "))
except ValueError:
    print("Ошибка! Введи число, не текст.")
else:
    print(f"Тебе {age} лет")  # выполняется если ошибки НЕ было
finally:
    print("Программа завершена") # выполняется ВСЕГДА


# Частые типы ошибок

# ValueError    # неверное значение → int("abc")
# ZeroDivisionError  # деление на ноль → 10 / 0
# FileNotFoundError  # файл не найден → open("нет.txt")
# IndexError    # индекс за пределами → list[100]
# KeyError      # ключ не найден → dict["нет"]
# json.JSONDecodeError  # сломанный JSON → json.load(пустой файл)


try:
    numbers = [1, 2, 3]
    result = numbers[10] / 0
except IndexError:
    print("Индекс за пределами списка!")
except ZeroDivisionError:
    print("Деление на нол")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")  # ловит всё остальное