class Mint:
    present_year = 2024
    present_bitch= 'Kelly'
    def __init__(self):
        self.year = Mint.present_year
        
    def create(self, coin_cls):
          # 这里写了更新
        return coin_cls(self.year)

   

    def update(self):
       self.year=Mint.present_year
       self.bitch=Mint.present_bitch
       print(f"Mint被修改到{self.year}")

mint=Mint()
print(mint.year)
print(mint.present_bitch)

Mint.present_year=2030
mint.update()
print(mint.year)
print(mint.present_year)

class NewMint:
    present_year = 2024
    present_bitch= 'Kelly'
    def __init__(self):
        self.update()

    def create(self, coin_cls):
        self.update()
        

    def refresh_stamp(self):
        self.update()

    def update(self):
        self.year=NewMint.present_year
        self.bitch= NewMint.present_bitch
        print(f"被更新了年份{self.year}")
        

NM=NewMint()
NM2=NewMint()
NM3=NewMint()
print(NM.present_year)
print(NM2.present_year)
print(NM.bitch)
print(NM2.bitch)
NewMint.present_bitch= 'Cathy'
NewMint.present_year=2030

NM.update()
NM2.update()
NM3.update()


print(NM.bitch)
print(NM2.bitch)
print(NM3.bitch)
print(NM.year)