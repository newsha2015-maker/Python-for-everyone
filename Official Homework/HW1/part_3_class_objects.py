# Part 3: Classes and Objects

# Create a class called BankAccount with attributes for account holder name, account number, and balance. 
# Include methods to deposit and withdraw money.
import statistics

class Bankaccount:
    def __init__(self, account_name, account_number, initial_balance = 0):  
        self.account_name = account_name
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient Funds. Availabe Balance ${self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

name = input("Enter account holder name: ")
number = input("Enter account number: ")
my_acc = Bankaccount(name, number)

