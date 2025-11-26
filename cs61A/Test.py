from unicodedata import name, lookup
print(lookup('WHITE SMILING Face'))
numeral={'A':12,'2':13,'J':11}

numeral['Joker']=9999

numeral['Joker']=10000

numeral.pop('Joker')



a=[1]
a.append(a)
print(a)
t=[1,2,3]
t[1:3]=t
print(t)