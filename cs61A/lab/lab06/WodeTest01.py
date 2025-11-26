import random
class GirlFriend:
    def __init__(self,name,height):
        self.name=name
        self.height=height
        

    def dating(self, caller):
        
        print(f"早上，{self.name}和{caller}在湖边见面")
       
    def profile(self):
        print(f"你好babe，我的名字叫{self.name},我身高{self.height}")

class GachaMachine():
    def __init__(self):
        self.names=["Alice","Cathy","Katie","Betty","Lily","Lexi","Victoria"]
        self.heights=list(range(167,179))
    
    def roll(self):
        name=random.choice(self.names)
        height=random.choice(self.heights)
        return GirlFriend(name,height)
    

machine = GachaMachine()
gf1=machine.roll()
gf1.dating("Kensho")
gf1.profile()
nums=[1,3,5,7,9]
