name = input("Как тебя зовут? ")
year = int(input("Сейчас какой год? "))
born_year = int(input("Какой тебе год рождения? "))

age = year - born_year

print(f"Привет! {name}, тебе {age} лет.")
