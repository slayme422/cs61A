"""def decoration(f):
    
    def inside(x):
        print(f'正在调用参数{x}的值')
        
        return f(x)
    return inside

def fib(n):
    if n==1 or n==0:
        return n
    return fib(n-2)+fib(n-1)
fib=decoration(fib)
print(fib(5))

def make_adder(n):
    def adder(x):
        return x+n
    return adder
"""

#mutation

"""x是分子 y是分母"""
def numerical(x,y):
    if not y:
        raise Exception("分母不能是0")
    else:
        return (x,y)
try:
    print(numerical(1, 2))
except Exception as e:
    print("错误",e)

#检查是否是列表
"""def check_list(s):
    if isinstance(s,list):
        return '没问题'
    else:
        raise Exception

try:
    print(check_list((1,2,3)))
except Exception as e:
    print(e)

print("我运行到这里了")"""

try:
    x=1/0
except Exception:
    print(Exception)
    x=0
print(x)


def oski(bear):
    def cal(berk):
        nonlocal bear
        if bear(berk) == 0:
            return [berk+1,berk-1]
        bear=lambda ley: berk - ley
        return [berk, cal(berk)]
    return cal(2)

print(oski(abs))

def repeat(f,n,x):
    if n==1:
        return 1
    return f(x) * repeat(f,n-1,x)

print(repeat(lambda x:x*x,2,5))