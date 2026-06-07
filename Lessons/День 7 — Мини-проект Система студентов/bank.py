trancations = [] 

def add_income(trancations):
    amount = int(input("Ваш даход: "))
    description = input("Описание: ")
    trancations.append({"type": "даход", "amount": amount, "description": description})

def add_expense(trancations):
    amount = int(input("Ваш расход: "))
    description = input("Описание: ")
    trancations.append({"type": "расход", "amount": amount, "description": description})

def show_trancations(trancations):
    if len(trancations) == 0:
        print("Ваш история пусто: ")
        return

    for t in trancations:
        print(f"{t['type']}: {t['amount']} - {t['description']}")

def show_balanse(trancations):
    income = sum(t["amount"] for t in trancations if t["type"] == "даход")
    expense = sum(t["amount"] for t in trancations if t["type"] == "расход")
    balance += income
    balance -= expense
    print(f"Даходы: {income}")
    print(f"Расходы: {expense}")
    print(f"Баланс: {balance}")


def main():
    balance = 0
    while True:
        print("\n1: Добавить доход")
        print("2: Добавить расход")
        print("3: Показать все транзакции")
        print("4: Показать баланс")
        print("5: Выйти")

        user_input = input("\nВыберите: ")

        if user_input == "1":
            add_income(trancations)
        elif user_input == "2":
            add_expense(trancations)
        elif user_input == "3":
            show_trancations(trancations)
        elif user_input == "4":
            show_balanse(trancations)
        elif user_input == "5":
            print("Выход!")
            break
        else:
            print("Невеный выбор!")


main()