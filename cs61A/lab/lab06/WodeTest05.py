class Account():
    interest=0.02
    withdraw_fee=1
    def __init__(self,account_holder):
        self.holder=account_holder
        self.balance=0

    def withdraw(self,amount):
        if amount > self.balance:
            return 'unsufficient funds'
        else:
            self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
class SavingAccount(Account):
    deposit_fee=2

    def deposit(self, amount):
        return Account(self, amount-self.deposit_fee)

        