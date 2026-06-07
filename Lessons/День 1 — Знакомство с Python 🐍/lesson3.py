name = "Азизжон"  # str  — строка (текст)
age = 18          # int  — целое число
height = 175.5    # float — дробное число
is_student = True # bool — True или False (да/нет)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# f-строка
print(f"Мне {age} лет")

#  конвертация
print("Мне " + str(age) + " лет") # str() превращает число в текст


int("18")      # текст → целое число
float("13.5")  # текст → дробное число
str(100)       # число → текст

name = input("Как тебя зовут?")
print(f"Привет {name}!")

age = input("Сколько тебе лет? ")
print(type(age))   # <class 'str'>  ← не int!

age = int(input("Cколько тебе лет? "))
print(type(age))   # <class 'int'>  ✅

