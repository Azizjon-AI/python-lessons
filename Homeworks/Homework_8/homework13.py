class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self):
        deposit = int(input("Сколько хотите попольнит: "))
        self.balance += deposit
        print(f"Пополнено: {deposit}. Баланс: {self.balance}")

    def withdraw(self):
        withdraw = int(input("Сколько хотите снять: "))
        if withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Снято: {withdraw}. Баланс: {self.balance}")
        else:
            print("Денег не хватает!")

    def show_balance(self):
        print(f"Баланс {self.owner}: {self.balance}")

def main():
    while True:
        owner = input("Как вас зовут: ")
        print(f"Привет, {owner}")
        account = BankAccount(owner)
        while True:
            print("\n1: Пополнить")
            print("2: Снять")
            print("3: Показать баланс")
            print("4: Назад")

            user_input = input("\nВыберите: ")

            if user_input == "1":
                account.deposit()
            elif user_input == "2":
                account.withdraw()
            elif user_input == "3":
                account.show_balance()
            elif user_input == "4":
                break
            else:
                print("Неверный ввод")

        exte = input("Для выход напишети 6. А для начала любой другой цифр: ")
        if exte == "6":
            print("Выход!!!")
            break
        else:
            print("Главное")

main()