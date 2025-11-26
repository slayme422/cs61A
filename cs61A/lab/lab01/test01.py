def search(f):
    x=0
    print("debug1:"+str(x))
    while True:
        print("debug2:"+str(x))
        if f(x):
            return x
        else:x+= 1

def square(x):
    return x * x

def positive(x):
    return max(0,square(x)-100)


print(search(positive))