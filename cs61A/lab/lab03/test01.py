from math import gcd
"""返回一个List[x,d] x是numerator, d是denominator
并且要求x,d要relative prime--x和d互质，共同因子只有1"""
def rational(x,d):
    div=gcd(x,d)
    if div!=1:
        return [x//div,d//div]
    else:
        return [x,d]
        
"""返回一个numerator"""
def numer(x):
    return x[0]

"""返回一个denominator"""
def denominator(d):
    return d[1]

print(rational(25,50))
print(rational(36,48))