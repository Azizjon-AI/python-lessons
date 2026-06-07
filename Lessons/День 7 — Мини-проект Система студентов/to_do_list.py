tasks = []

def add_task(tasks):
    task = input("Какой задача на сегодния: ")
    tasks.append({"id": len(tasks) + 1, "title": task, "done": False})

def show_tasks(tasks):
    if len(tasks) == 0:
        print("Список пусто!")
        return
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        print(f"[{task['id']}: {status} - {task['title']}]")

def complete_task(tasks):
    if len(tasks) == 0:
        print("Список пуст!")
        return

    complete = int(input("Введите id задачи: "))
    
    found = False  
    
    for t in tasks:
        if complete == t["id"]:
            t["done"] = True
            found = True  
            print(f"Задача '{t['title']}' выполнена ✅")
            break  
    
    if not found:
        print("Такой id не существует!")

def delete_task(tasks):
    if len(tasks) == 0:
        print("Список пусто!")
        return

    delete = int(input("Введите id задачи: "))

    found = False

    for t in tasks:
        if delete == t["id"]:
            tasks.remove(t)
            found = True
            print(f"Задача {t['title']} удалено!")

    if not found:
        print("Такой id не существует")
            


def statistics(tasks):
    complete = sum(1 for t in tasks if t["done"] == True)
    donot_complete = sum(1 for t in tasks if t["done"] == False)
    print(f"Всего задач: {len(tasks)}")
    print(f"Выполнено: {complete}")
    print(f"Осталось: {donot_complete}")

def main():
    while True:
        print("\n1: Добавить задачу")
        print("2: Показать все задачи")
        print("3: Отметить задачу выполненной")
        print("4: Удалить задачу")
        print("5: Показать статистику")
        print("6: Выйти!")        

        user_input = input("\nВыберите: ")
        
        if user_input == "1":
            add_task(tasks)
        elif user_input == "2":
            show_tasks(tasks)
        elif user_input == "3":
            complete_task(tasks)
        elif user_input == "4":
            delete_task(tasks)
        elif user_input == "5":
            statistics(tasks)
        elif user_input == "6":
            print("Выход!")
            break
        else:
            print("Неправылный ввыод!")

main()

    