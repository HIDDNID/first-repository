class Account:
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счёте")
        else:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    def get_balance(self):
        print(f"Текущий баланс - {self.balance}")

# Создание экземпляра класса
account = Account("12323132", 600)

# Пополнение баланса
account.deposit(100)

# Снятие средств
account.withdraw(2000)

# Проверка текущего баланса
account.get_balance()

account.deposit(5000)

account.withdraw(2800)
