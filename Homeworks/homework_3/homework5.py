# Подсказка — структура:

secret = 7  # загаданное число

guess = int(input("Угадай число: "))

while guess != secret:
    print("Попробуй ещё раз")
    guess = int(input("Угадай число: "))

print("Правильно! 🎉")