# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег.

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.tax_rate = 0.10
        self.tax_threshold = 5000000

    def deposit(self, amount):
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратна 50 у.е.")
            return
        self.balance += amount
        self.transactions.append(f"Пополнение: +{amount} у.е.")
        print(f"Вы пополнили счёт на {amount} у.е. Баланс: {self.balance} у.е.")

    def withdraw(self, amount):
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратна 50 у.е.")
            return
        if self.balance < amount:
            print("Недостаточно средств на счете.")
            return
        self.balance -= amount
        fee = max(30, min(amount * 0.015, 600))  # Рассчитываем комиссию
        self.balance -= fee
        self.transactions.append(f"Снятие: -{amount} у.е. (комиссия: -{fee} у.е.)")
        print(f"Вы сняли {amount} у.е. (комиссия: {fee} у.е.) Баланс: {self.balance} у.е.")

    def apply_tax(self):
        if self.balance >= self.tax_threshold:
            tax_amount = self.balance * self.tax_rate
            self.balance -= tax_amount
            self.transactions.append(f"Удержан налог на богатство: -{tax_amount} у.е.")

    def display_balance(self):
        self.apply_tax()
        print(f"Баланс: {self.balance} у.е.")

    def display_transactions(self):
        print("История операций:")
        for transaction in self.transactions:
            print(transaction)


def main():
    account = BankAccount()

    while True:
        print("\nВыберите действие:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Показать баланс")
        print("4. Показать историю операций")
        print("5. Выйти")
        choice = input()

        if choice == '1':
            amount = float(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            account.display_transactions()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
