from abc import ABC, abstractmethod


class Person:
    def __init__(self, name):
        self.name = name


class Account(ABC):
    def __init__(self, Person):
        self.name = Person.name
        self._balance = 0
    @property
    def balance(self):
        return f"your balance with the name of {self.name} is {self._balance}"
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Amount cannot be greater than balance")
        self._balance -= amount
    @abstractmethod
    def calculate_benifit(self):
        pass


class SavingAccount(Account):
    def calculate_benifit(self, benefit_rate):
        return f"{((benefit_rate / 100) * self._balance)} should be paid anually"


class CurrentAccount(Account):
    def calculate_benifit(self, benefit_rate):
        return f"{((benefit_rate / 100) * self._balance)} should be paid anually"


person1 = Person("Ahmad")
account1 = SavingAccount(person1)
account1.deposit(1000)
account1.withdraw(100)
print(account1.calculate_benifit(2))
print(account1.balance)

person2 = Person("Amir")
account2 = CurrentAccount(person2)
print(account2.balance)
account2.deposit(10000)
account2.withdraw(1000)
print(account2.calculate_benifit(5))
print(account2.balance)