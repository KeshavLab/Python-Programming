

class BankAccount:

    # constructor
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    # method for deposite
    def deposite(self,amount):
        if(amount>0):
            self.balance=self.balance+amount
            print(f"Deposited :{amount}")

    def withdraw(self,amount):
        if amount <self.balance:
            self.balance=self.balance-amount
            print(f"the withdraw amount is {amount} ")
        

    # function to show balance 
    def show_balance(self):
        print(f"Current balance is :{self.balance}")


# object create karana hai
account1=BankAccount("keshav",20000)

# deposite money
account1.deposite(1000)

#withdraw
account1.withdraw(2000)

# check balance
account1.show_balance()