def average(retings):
    return sum(retings) / len(retings)

print(average([4, 5, 2, 3, 4]))
print(average([5, 3, 2, 4, 2]))
print(average([5, 2, 3, 4, 3]))

# Примеры

# Без параметров:
def great():
    print("Привет")

great() # Привет
great() # Привет

# С параметрами:

def great(name):
    print(f"Привет! {name}")

great("Ali")       # Привет! Ali
great("Azizjon")   # Привет! Azizjon

# С return:

def add(a, b):
    return a + b

result = add(4, 5)
print(result)

# Важная разница — print vs return:
def bad(a, b):   
    print(a + b)   # просто выводит, ничего не возвращает

def good(a, b):
    return a + b  # возвращает результат — можно сохранить

x = bad(2, 4)  # y = None  ❌
y = good(5, 3) # x = 8  ✅

print(x)
print(y)
