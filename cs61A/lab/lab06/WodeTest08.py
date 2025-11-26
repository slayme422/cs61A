from math import gcd
class GirlFriend:
    present_year=2024
    def __init__(self, name, height):
        self.name=name
        self.height=height
    
    def profile(self):
        return f'hey宝贝,我的名字是: {self.name},我的身高是{self.height}'
    
    def update(self):
        "*** YOUR CODE HERE ***"
        year=self.present_year
        return year
g1=GirlFriend('Kathy',174)

g2=GirlFriend('Alicia',175)

girlfriends={g1.name: g1, g2.name:g2}

