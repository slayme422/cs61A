arr1=[[],[1,2,3,4,6]]
arr1=arr1[1:]
print(arr1)
arr1.append(arr1.extend(arr1[:1]))
print(arr1)
print(id(arr1[0]), id (arr1[1]))