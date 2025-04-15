class BankAccount:
    accounts: list["BankAccount"] = []

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")

        self._balance = balance
        self.number = id(self)
        BankAccount.accounts.append(self)

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance: int):
        raise AttributeError("Can't set attribute")

    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")

        self._balance += amount

    def withdraw(self, amount: int):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")

        if self.balance < amount:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")

        self._balance -= amount

    def transfer(self, other: "BankAccount", amount: int):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")

        if self.balance < amount:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")

        self._balance -= amount
        other._balance += amount

    def __repr__(self):
        return f"BankAccount(balance={self.balance})"


a1 = BankAccount()
print(a1.balance)

a1.deposit(10)
print(a1.balance)

a2 = BankAccount(balance=20)
a2.withdraw(15)
print(a2.balance)

a1.transfer(a2, 3)
print(a1)
print(a2)

# a1 = BankAccount(-10)
# a1 = BankAccount(10)
# a1.withdraw(-5)
# a1.withdraw(50)
# a1.deposit(-5)

# a2 = BankAccount(balance=20)
# a1.transfer(a2, 100)

a1 = BankAccount(100)
a2 = BankAccount()
print(a1.number)
print(a2.number)
a3 = BankAccount(50)
print(a3.number)

print(BankAccount.accounts)
print(a1.transfer(a3, 15))
print(BankAccount.accounts)

a1 = BankAccount(100)
print(a1.balance)
# a1.balance = 500
# print(a1.balance)
a1.deposit(400)
print(a1.balance)
