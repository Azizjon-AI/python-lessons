class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        
    def average(self):
        return sum(self.grades) / len(self.grades)


    def show_info(self):
        print(f"Имя {self.name}, Средный балл {self.average()}")

s = Student("Azizjon")
s.add_grade(99)
s.add_grade(88)
s.add_grade(77)
s.add_grade(66)
s.show_info()