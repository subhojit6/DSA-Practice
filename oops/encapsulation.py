class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(self._balance)

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(self._balance)


account = BankAccount(1000)

print(account.balance)


