class Animal:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест")
    
    def sleep(self):
        print(f"{self.name} спить")

class Dog(Animal):
    def __init__ (self, name, age, breed): # добавляем породу
        super().__init__ (name, age)       # вызываем Animal.__init__
        self.breed = breed                 # добавляем свой атрибут
        print(f"{self.name} лает: Гав!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} мяукает: Мяу")

dog = Dog("Рекс", 3, "Овчарка")
cat = Cat("Мурка", 2)

dog.eat()   # Рекс ест       ← метод от Animal
# dog.bark()  # Рекс лает: Гав! ← свой метод
print(dog.breed)

cat.sleep() # Мурка спит     ← метод от Animal
cat.meow()  # Мурка мяукает  ← свой метод


class Animal:
    def speak(self, name, age):
        self.name = name
        self.age = age
        print("....")

class Dog(Animal):
    def speak(self):
        print("Гав!")

class Cat(Animal):
    def speak(self):
        print("Мяу!")

animals = [Dog("Рекс", 3), Cat("Мурка", 2)]

for animal in animals:
    animal.speak()

