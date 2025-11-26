class Account():
    interested=0.02
    def __init__(self,account_holder):
        self.balance=0
        self.holder=account_holder

    def withdraw(self,amount):
        if amount>self.balance:
            return 'insufficient Fund'
        
        self.balance=self.balance-amount
        return self.balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
class CheckingAccount(Account):
    withdraw_fee=1
    interest= 0.01
    def __init__(self, account_holder):
        super().__init__(account_holder)
    def withdraw(self, amount):
        return Account.withdraw(self,amount+self.withdraw_fee)
    
ch=CheckingAccount('Eric')
ch.deposit(1000)
print(ch.balance)
print(ch.withdraw(800))
print(ch.balance)
