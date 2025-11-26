def p1(s):
    """
    找出绝对值最小的值的索引
    >>>t=[-4, -3, -2, 3, 2, 4]
    [2,4]
    >>>[1,2,3,4,5]
    [0]
    """ 
    min_abs=min(map(abs,s))
    list1=[x for x in range(len(s)) if abs(s[x])==min_abs]
    
    return list1
def p2(t):
    """
    找出数组中任意相邻两个整数值的和是最大的 值
    >>> [-4,-3,-2,3,2,4]
    6
    """
    
    sum_t=[t[i]+t[i+1] for i in range(len(t)) if i<len(t)-1]
    return max(sum_t)

def p3(t):
    dictionary={}
    for i in range(len(t)):
        dictionary[i]=t[i]
    return dictionary

def p4(t):
    """每个元素是否有其他相等的元素
    >>> p4([-4,-3,-2,3,2,4])
    False
    >>> [4,3,2,3,2,4]
    True
    """
    all([t[i] in t[:i]+t[i+1:] for i in range(len(t))])
t=[4,3,2,3,2,4,4]


print(min([sum([1 for y in t if y==x]) for x in t])>2)

arr=[]
print(len(arr)==0)