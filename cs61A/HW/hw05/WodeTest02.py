items,n=[],2

class Airpods:
    cost,k = 200,0
    f = lambda self:print(self)

    def __init__(self):
        Airpods.k +=1
        Airpods.f(self)
        items.extend([self])
    
    def __repr__(self):
        return (Airpods.k<2 and "lonely") or "pair"

class TwoAirpods(Airpods):
    def __init__(self):
        self.k=2
        Airpods.__init__(self)
        Airpods.__init__(self)
    
def discount(a):
    a.cost//=2
    
def u(w,u):
    return [print(u) for u in [w,u]]
    
discount(Airpods)

print(TwoAirpods.cost)
lost=Airpods()
willbelost= TwoAirpods()
str(lost)
print([item.k for item in items])
print(u(lost,willbelost))