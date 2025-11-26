def first(n=1):
    print(f"你正在使用第{n}个函数")
    n=n+1
    return second(n)

def second(n):
    print(f"你正在使用第{n}个函数")
    n=n+1
    return third(n)

def third(n):
    print(f"你正在使用第{n}个函数")
    return '密码1905'
    
print(first())

