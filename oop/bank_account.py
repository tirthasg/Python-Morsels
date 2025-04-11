class BankAccount:
    accounts: list["BankAccount"] = []

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")

        self._balance = balance
        self.number = id(self)
        BankAccount.accounts.append(self)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        raise AttributeError("Can't set attribute")

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")

        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")

        if self.balance < amount:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")

        self._balance -= amount

    def transfer(self, other, amount):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")

        if self.balance < amount:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")

        self._balance -= amount
        other._balance += amount

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"
