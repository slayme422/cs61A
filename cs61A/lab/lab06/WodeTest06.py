def tree(label,branches=[]):
    for b in branches:
        if not is_tree(b):
            return False
    return [label]+list(branches)

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_tree(t):
    for b in branches(t):
        assert len(b)>1 and b

    

print(tree(1,[tree(1),tree(3)]))


from math import gcd
def rational(x,d):
    div=gcd(x,d)
    if div !=1:
        return [x//div,d//div]
    
    else:
        return [x,d]
    
print(rational(4,8))

def numer(x):
    return x[0]

def denominator(d):
    return d[1]

def mul(x,y):
    
    return rational(numer(x) * numer(y),denominator(x) * denominator(y))

print(mul(rational(1,6),rational(3,7)))