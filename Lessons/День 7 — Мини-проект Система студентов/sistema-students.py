students = []  

def add_student(students):
    name = input("Как тебя зовут: ")
    grade = int(input("Сколбко баллов вы забралы: "))
    students.append({"name":name, "grade": grade})
    


def show_students(students):
    for student in students:
        print(f"Имя {student['name'].title()}, {student['grade']} баллов.")


def best_student(students):
    if len(students) == 0:
        print("Список пуст!")
        return

    best = students[0]
    for student in students:
        if student["grade"] > best["grade"]:
            best = student

    print(f"Лучший студент: {best['name'].title()} - {best['grade']} баллов")

def menu():
    while True:
        print("\n1. Добавить студента")
        print("2. Показать всех")
        print("3. Лучший студент")
        print("4. Выйти")
        
        choice = input("\nВыберите: ")
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            best_student(students)
        elif choice == "4":
            print("Пока!")
            break
        else:
            print("Неверный выбор!")

menu()