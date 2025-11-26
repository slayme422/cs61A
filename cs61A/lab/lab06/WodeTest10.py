class Ratio:
    def __init__(self,n,d):
        self.numer= n
        self.denom= d

    def __repr__(self):
        return 'Ratio({0},{1})'.format(self.numer,self.denom)
    
    def __str__(self):
        return '{0}/{1}'.format(self.numer,self.denom) 

print(Ratio(1,2))

class Kangaroo:
    def __init__(self):
        self.pouch_contents=[]

    def put_in_pouch(self, obj):
        if obj in self.pouch_contents:
            return 'object already in pouch'
        
        self.pouch_contents.append(obj)

    def __str__(self):
        if self.pouch_contents==[]:
            return 'The Kangaroo\'s pouch is empty'
        
        return 'The kangaroo\'s pouch contains: {}'.format(self.pouch_contents)
        
kangaroo_k1=Kangaroo() 
kangaroo_k1.put_in_pouch("a")
kangaroo_k1.put_in_pouch("b")

kangaroo_k1.put_in_pouch("baby")

def countup():
    n=0
    while True:
        
        yield n
        n=n+1
        
        



g=countup()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def print_name(name):
    for i in name:
        yield i 

p1=print_name("Kensho")
print(next(p1))
print(next(p1))
print(next(p1))
print(next(p1))
print(next(p1))
print(next(p1))
print(next(p1))