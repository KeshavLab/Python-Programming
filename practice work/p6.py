class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance


    def deposit(self,amount):
        if(amount>0):
            self.balance=self.balance+amount
            print(f"Deposited amount {amount}")

    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance=self.balance-amount
            print(f"Withdraw amount is {amount}")

    def show_balance(self):
        print(f"the current balance is {self.balance}")



b=BankAccount("keshav",2000)
b.deposit(100)
b.withdraw(50)
b.show_balance()