def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2) + fib(n-1)
    
def count(f):
    def counted(n):
        counted.call_count+=1
        return f(n)
    counted.call_count=0
    return counted
#给f做一个包装，让我每次玩函数的时候自动打印一个，小日最帅,这个函数可以带x

def glory(f):
    def g(x):
        print("小日真帅")
        return f(x)
    return g
fib=glory(fib)
fib(5)
def memo(f):
    cache={}
    def memoized(n):
        if n not in cache:
            cache[n]=f(n)
        return cache[n]
    memoized.cache= cache
    return memoized    

