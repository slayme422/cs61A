dictionaries={}
dictionaries[0]="chalice"
dictionaries[1]="Alice"
dictionaries[1]="Kensho"
print(dictionaries)


name="wangxiyao"

for i in range(len(name)):
    print(name[:len(name)-i])

d={'id':1 , 'progress':0.75}
g={'id':2 , 'progress':0.4}
x={'id':3 , 'progress':0.8}
print(d)
print(d['id'])
print(d['progress'])
print(g['id'])
print(g['progress'])
print_progress= lambda d: print('ID:',d['id'],'Progress:',d['progress'])

print(print_progress(d))
print(print_progress(g))
print(print_progress(x))
print(print_progress({'id':4,'progress':0.7}))