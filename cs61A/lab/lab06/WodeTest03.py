class Account:
    interest=0.02
    def __init__(self, account_holder):
        self.holder=account_holder
        self.balance=0

    def deposit(self, amount):
        self.balance=self.balance+amount
        return self.balance

    def withdraw(self, amount):
        if amount>self.balance:
            return 'Insufficient Funds'
        self.balance=self.balance-amount
        return self.balance
    
    class CheckingAccount(Account):
        withdraw_fee=1
        interest=0.01
        
        def withdraw(self, amount):
            return Account.withdraw(self, amount+self.withdraw_fee)

"""银行开户"""   
class Bank: 
    def __init__(self):
        self.accounts=[]

    """kind种类把参数限制成某一特别类型"""
    def open_account(self,holder,amount,kind=Account):
        account=kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)