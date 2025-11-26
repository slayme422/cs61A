"""创造一个分母denominator:d和一个分子numerator:n"""
from math import gcd
def rational(n,d):
    g=gcd(n,d)
    return [n //g,d//g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def mul_rational(x,y):
    return rational(numer(x) *numer(y),denom(x) * denom(y))

