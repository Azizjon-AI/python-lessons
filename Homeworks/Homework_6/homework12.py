students = [
    {"name": "Azizjon", "grade": 99},
    {"name": "Omina", "grade": 89},
    {"name": "Dusmurod", "grade": 70}
]

best = students[0]

for student in students:
    if student["grade"] > best["grade"]:
        best = student

print(f"Лучший студент {best['name']}: {best['grade']} баллов")