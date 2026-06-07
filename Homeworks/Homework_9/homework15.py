class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Сотрудник: {self.name}, зарплата {self.salary}")

    def give_raise(self, amount):
        self.salary += amount
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f"Менеджер: {self.name}: Атдел: {self.department}, Зарплата: {self.salary}")

    def hire(self, employee_name):
        print(f"{self.name} нанял {employee_name}")


class Intern(Employee):
    def __init__(self, name, salary, university):
        super().__init__(name, salary)
        self.university = university

    def show_info(self):
        print(f"Стажёр: {self.name}, университет: {self.university} зарплата: {self.salary}")

    def study(self):
        print(f"{self.name} учится и работает")


employee = Employee("azizjon", 100)
employee.show_info()
employee.give_raise(500)
employee.show_info()

manager = Manager("Kamol", 2000, "IT")
manager.show_info()
manager.hire("Azizjon")

intern = Intern("Sanjar", 200, "ТНУ")
intern.show_info()
intern.study()