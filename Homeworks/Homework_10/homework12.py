import json
import os

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)


    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)
 
    def show_info(self):
        print(f"Имя {self.name}, Средний бал {self.average()}")

def save_students(students):
    data = []
    for s in students:
        data.append({"name": s.name, "grades": s.grades})

    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_students():
    if not os.path.exists("students.json"):
        return []

    with open("students.json", "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    students = []
    for d in data:
        s = Student(d["name"])
        s.grades = d["grades"]
        students.append(s)

    return students

def main():
    students = load_students()

    while True:
        print("\n1 - Добавить студент")
        print("2 - Показать всех")
        print("3 - Выйти")

        choise = input("\nВыберите: ")

        if choise == "1":
            name = input("Имя студента: ")
            grades = []
            while True:
                print("\n1 - Добавить бал")
                print("2 - Дале")
                
                choise = input("\nВыберите: ")
                if choise == "1":
                    grade = int(input("Добавить бал: "))
                    grades.append(grade)
                elif choise == "2":
                    print("Выход!")
                    break
                else:
                    print("\nНе правилный ввод!")

            student = Student(name)
            student.grades = grades
            students.append(student)
            save_students(students)

        elif choise == "2":
            for s in students:
                s.show_info()

        elif choise == "3":
            print("Выход!")
            break

        else:
            print("Не правилный ввод!")

main()
