import json

students = [
    {"name": "Azizjon", "grade": 95},
    {"name": "Ali", "grade": 88}
]

# Сохранить:
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file)

# Загрузить:
with open("students.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded) 