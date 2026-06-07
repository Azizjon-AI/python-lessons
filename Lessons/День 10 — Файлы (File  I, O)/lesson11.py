# Записать в файл: 

file = open("notes.txt", "w", encoding="utf-8")
file.write("Привет, файл")
file.close()

# Прочитать файл:

file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
file.close()
print(content)

"r"  # read    — читать
"w"  # write   — записать (удаляет старое!)
"a"  # append  — добавить в конец

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Привет\n")
    file.write("Это второя строка.\n")

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip()) 

