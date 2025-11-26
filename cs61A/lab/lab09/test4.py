def repeat(f,n,x):
    if n==0:
        return 1
    return f(x) * repeat(f,n-1,x)

print(repeat(lambda x:x*x,2,5))

"""
定义gcd 找出最大公因数
>>> gcd(6 4) 
2
#gcd(6 4) a=6 b=4 d=2 判断进去else->gcd(4 2) 判断 d=0 返回2位最大因数
#gcd(16 12)
4
"""

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
print(gcd(5,0))
print(gcd(16,12))
(define (gcd a b)
 (if(= 0 b)
  b
  (gcd b (modulo a b))))