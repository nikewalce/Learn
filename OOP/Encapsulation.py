"""
Инкапсуляция
Объединение данных и методов в одном классе, а также ограничение доступа к этим данным.
Пример: Закрытые свойства (с помощью _ или __). защита данных от некорректного использования (например, банковские счета, авторизация)."""


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Закрытое свойство

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance


# Использование
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Вывод: 1300