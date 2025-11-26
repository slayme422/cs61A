def fast_overlap(s,t):
    """返回一个s和t的重叠次数
    >>>fast_overlap([3,4,6,7,9,10],[1,3,5,7,8])
    2
    """
    i,j,count=0,0,0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            count,i,j=count+1,i+1,j+1
        elif s[i]<t[j]:
            i=i+1
        else:
            j=j+1
    return count
print(fast_overlap([3,4,6,7,9,10],[1,3,5,7,8]))
arr=[1,4,9]
arr.append(arr.extend(arr[:1]))#1,4,9,1
print(arr)