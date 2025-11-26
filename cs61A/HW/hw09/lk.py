class Frame:
    def __init__(self,parent=None):
        self.parent=parent
        self.bindings={}
    def define(self,key,value):
        self.bindings[key]=value
        return key
    def lookup(self,key): 
            if key in self.bindings:
                return self.bindings[key]
            elif self.parent:
                return self.parent.lookup(key)
            else:
                raise 'Error'

f1=Frame()
f2=Frame(f1)

f1.define("x",1)
print(f2.lookup("x"))