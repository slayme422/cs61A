from datetime import datetime 
now=datetime(2025,7,10)

until=datetime(2025,8,19)
length=now-until
print(f"还有{length}天")

lst = [1, 2, 3, 4]
copy_lst = lst[:]

for i in copy_lst:
    print(i)
    if i == 2:
        lst.remove(2)
