class Task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.done = False

    def complete(self):
        self.done = True
        print(f"Задача '{self.title}' выполнена ✅")

task = Task(1, "Учить python")
task.complete()

# Структура класса
class Название:
    def __init__(self, параметры):  # конструктор
        self.атрибут = значение     # данные объекта
    
    def метод(self):                # функция объекта
        kod

#  __init__ — вызывается автоматически при создании объекта
#  self — это сам объект, всегда первый параметр
#  self.x — атрибут объекта


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет мне зовут {self.name}, мне {self.age} лет")

    def birthday(self):
        self.age += 1
        print(f"{self.name}, теперь {self.age} лет.")

azizjon = Person("Azizjon", 18)
ali = Person("Ali", 16)

azizjon.greet()
ali.greet()
azizjon.birthday()
ali.birthday()

students = [
    Person("Азизжон", 18),
    Person("Али", 20),
    Person("Санжар", 19)
]

for student in students:
    student.greet()
    student.birthday()