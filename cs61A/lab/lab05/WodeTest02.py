def double(x):
    return x*2

m=map(double,range(3,7))

f=lambda y: y%4==0
t=filter(f,m)



a=[1,3,5,7]


g=filter(lambda x:(x**0.5)**2==x,[2,4,6,16])
print(list(g))
names=['Alice','Bob','Kensho']
scores=[66,77,99]
b=dict(zip(names,scores))
print(b)
