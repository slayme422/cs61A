
def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
    i=0
    count=1
    while i< len(s):
        if s[i] == before:
            s.insert(i+1,after)
            i+=1
        
        i+=1
        print(f'第{count}次的s数组长度{len(s)}')  
        count+=1
        print("i的长度"+str(i))
    return s

s = [1, 5, 5, 3,5]
for i in range(len(s)):
    if s[i] == 5:
        s.insert(i+1, 7)
        i+=1
    print(s)


t=iter(s)

for i in t:
    print(i)