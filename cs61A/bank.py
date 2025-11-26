import time
"""
下面是Account类
Account:Account的构造函数接受三个变量:
        self
        account_holder-> 账户持有者的姓名
        balance->账户的余额
balance是账户余额

"""
class Account:
    def __init__(self, account_holder,balance):
        self.holder = account_holder
        self.balance= balance
    def withdraw(self,amount):
        print(f'您的账户目前余额是{self.balance}')
        time.sleep(2)
        if amount > self.balance:
            return '提取失败,您的账户余额不足'
        else:
            self.balance=self.balance-amount
            return f'您的账户余额还剩{self.balance}'

    def deposit(self,amount):
        time.sleep(1)
        self.balance=self.balance+amount  
        return f'储存成功，账户余额为{self.balance}'
a1=Account('Tom',1000)

print(getattr(a1,'balance'))
print(hasattr(a1, 'balance'))