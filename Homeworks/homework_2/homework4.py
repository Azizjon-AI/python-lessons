name = input("Как вас зовут? ")
point = int(input("Сколько баллов вы набрали? "))

if point >= 90:
    grade = "Отлично"
elif point >= 70:
    grade = "Хорошо"
elif point >= 50:
    grade = "Удовлетворительно"
else:
    grade = "Неудовлетворительно"

print(f"{name}, ваш балл {point}. Оценка: {grade}.")