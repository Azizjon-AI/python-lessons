person = {
    "name": "Azizjon",
    "age": 18,
    "city": "Khujand"
}

print(person["name"])
print(person["age"])
print(person["city"])

person["email"] = "azizjon@gmail.com"  # добавить новый ключ
person["age"] = 19                     # изменить существующий

print(person["email"])
print(person["age"])

del person["city"]  # удалит

if "name" in person:
    print("Есть!")

print(person["name"])
print(person["age"])
# print(person["city"]) # вдаёт ошибку

for key, value in person.items():
    print(f"{key}: {value}")

students = [
    {"name": "Azizjon", "grade": 95},
    {"name": "Ali", "grade": 78},
    {"name": "Sanjar", "grade": 88}
]

for student in students:
    print(f"{student["name"]} - {student["grade"]} баллов")