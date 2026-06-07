import os 

def get_note():
    return input("Какие плани на сегодня: ")

def add_note(note):
    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")

def show_note():
    if not os.path.exists:
        print("Дневник пуст!")
        return
    with open("diary.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

def main():
    while True:
        print("\n1 - Добавить запись")
        print("2 - Показать все записи")
        print("3 - Выйти")

        choise = input("\nВыберите: ")

        if choise == "1":
            note = get_note()
            add_note(note)
        elif choise == "2":
            show_note()
        elif choise == "3":
            print("Выход!")
            break
        else:
            print("Неверный ввод!")

main()
