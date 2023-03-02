#create a python class called BankAccount with attributes like account_number,balance,date_of_opening and customer_name and
#methods like deposit,withdraw, check_balance and customer_details.
#i.The deposit method should return the amount deposited.
#ii.The withdraw method return insufficient balance if account balance is less than amount to be withdrawn else it 
#should return the amount that has been withdarwn.
#iii.The check_balance method should print the current balance.
#iv.The customer_details method should print customer name,account number,date of account openings and balance.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. Current balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. Current balance is {self.balance}.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")



account = BankAccount()

while True:
    action = input("What would you like to do? (deposit, withdraw, check_balance, quit) ")

    if action == "deposit":
        amount = float(input("How much would you like to deposit? "))
        account.deposit(amount)

    elif action == "withdraw":
        amount = float(input("How much would you like to withdraw? "))
        account.withdraw(amount)

    elif action == "check_balance":
        account.check_balance()

    elif action == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")