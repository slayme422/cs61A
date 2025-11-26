def no_repeats(lst):
    if not lst:
        return []
    head = lst[0]
    filtered_rest=[x for x in lst[1:] if x!=head]#[4,5]->[5]
    #lst[0:]是[2,4,4,5]
    return [head] + no_repeats(filtered_rest)

print(no_repeats((1,2,4,4,5)))
arr=[1,2,3,4,5]#我只想要[1,2,3] [5]
arr_left=arr[:3]#左进右出
arr_right=arr[4:]
print("左边的数组{0}和右边的数组{1}".format(arr_left,arr_right))