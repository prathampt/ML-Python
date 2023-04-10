Problem_Statement = """Exercise: Simple Banking System
Create a Python program that simulates a simple banking system. The program should have the following classes:

Account: an abstract base class with abstract methods deposit, withdraw, and get_balance.
SavingsAccount: a concrete class that inherits from Account and has a private attribute interest_rate and a concrete method add_interest.
CurrentAccount: a concrete class that inherits from Account and has a private attribute overdraft_limit and a concrete method get_overdraft_limit.
Customer: a class that holds a collection of accounts and has methods to add and remove accounts, 
as well as to calculate the total balance of the accounts.
Transaction: a decorator class that adds a fee to a withdrawal or deposit.
Use the classes to simulate a simple banking system where customers can open savings and current accounts, 
deposit and withdraw money, and add fees to certain transactions.

Try to use OOP concepts such as encapsulation, inheritance, and abstraction to create a well-structured and modular program.
You can also use decorators to add additional functionality to the classes."""

from abc import ABC,abstractmethod

class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

def Transaction(func):
    def wrapper(*args):
        amount = args[1]
        fee = 0.01 * amount
        print(f"Rs. {fee} were deducted from your account for the trasaction {func.__name__}")
        args = list(args)
        args.append(fee)
        return func(*args)
    return wrapper

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    @Transaction
    def deposit(self, amount, fee=0):
        self.balance += amount
        self.balance -= fee
        print("Rs.",amount, "is depostied into your bank account.")

    @Transaction
    def withdraw(self, amount, fee=0):
        if (amount+fee)<self.balance:
            self.balance -= amount
            self.balance -= fee
            print("Rs.",amount, "is withdrawn from your bank account.")
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.balance

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Rs.",interest, "is depostied into your bank account as intrest.")




class CurrentAccount(Account):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    @Transaction
    def deposit(self, amount, fee=0):
        self.balance += amount
        self.balance -= fee
        print("Rs.",amount, "is depostied into your bank account.")


    @Transaction
    def withdraw(self, amount, fee=0):
        if (amount+fee)<self.balance and amount<self.overdraft_limit:
            self.balance -= amount
            self.balance -= fee
            print("Rs.",amount, "is withdrawn from your bank account.")
        elif amount>self.balance:
            print("Insufficient Balance!")
        else:
            print("Overdraft Limit Exceeded!")

    def get_balance(self):
        return self.balance

    def get_overdraft_limit(self):
        print(self.overdraft_limit)


class Customer :
    account_dict = {}

    def add_account(self,account_number,name,actype,balance):
        account_dict[account_number] = [name,actype,balance]

    def remove_account(self,account_number):
        del account_dict[account_number]

    @staticmethod
    def get_total_balance():
        sum = 0
        for name,actype,balance in self.account_dict.values():
            sum += balance

        return sum

if __name__ == "__main__":
    prat = SavingsAccount("Pratham", 10000000, 5)
    prat.deposit(100)
    prat.add_interest()
    prat.withdraw(10000)
    print("Remaining balance: ", prat.get_balance())