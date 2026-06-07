names = ["Azizjon", "Ali", "Sanjar", "Zafar"]

print(names[0])   # Azizjon  ← индексы начинаются с 0!
print(names[1])   # Ali
print(names[2])   # Sanjar
print(names[3])   # Zafar
print(names[-1])  # Zafar ← -1 это последний элемент

print(len(names))

# Добавить элемент:
names.append("Kamol") 
print(names)   # ["Azizjon", "Ali", "Sanjar", "Zafar", "Kamol"]

# Удалить элемент:
names.remove("Ali")
print(names)   # ["Azizjon", "Sanjar", "Zafar", "Kamol"]