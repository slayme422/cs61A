class Account:
    withdraw_fee=1
    #构造器
    def __init__(self,holder,phone_number,person_id):
        self.account_holder=holder
        assert len(phone_number)==11
        self.phone_number=phone_number
        self.person_id=person_id
        
        self.balance=0
        
    def deposit(self,amount):
        self.balance= self.balance+amount
        return self.balance
    #账户余额减去钱数再减去手续费

    def withdraw(self,amount):
        if amount>self.balance:
            return 'unsufficient funds'
        else:
            self.balance=self.balance-amount-self.withdraw_fee
            return self.balance
        
class Bank:
    bank_policy='所有银行必须遵守的协议'
    def __init__(self,bank_name):   
        self.accounts=[]
        self.bank_name=bank_name
 
    def open_account(self,person_name,phone_number,person_id):
        self.accounts.append(Account(person_name,phone_number,person_id))

    def print_all_account(self):
        for account in self.accounts:
            print("正在打印花旗银行列表下的用户信息")
            print("此账户持有人: "+str(account.account_holder))
            print("电话号码: "+str(account.phone_number))
            print("身份id: "+str(account.person_id))
            print("目前金额: "+str(account.balance))
            print("--------------------")

   
citybank=Bank("CityBank")
b2=Bank("中国银行")

#我想在花旗银行下开户
citybank.open_account("曾宪昭","18519714917","110102199712153318")
print(citybank.accounts[0].deposit(100))
print(citybank.accounts[0].withdraw(50))

citybank.open_account("Kensho","09088511597","99999")

citybank.print_all_account()


