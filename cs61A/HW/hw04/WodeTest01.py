


        #先给他排序,去重
def longestConsecutive(nums) -> int:
    if not nums:
        return 0
    
    nums=sorted(set(nums))

    current_longest_sequence=1
    prev,curr=0,1
    cur_length=1
    while curr<len(nums):
        if nums[prev]+1!=nums[curr]:#判断是否是连续的
            cur_length=1
        else:
            cur_length=cur_length+1
        prev,curr=prev+1,curr+1
        current_longest_sequence=max(current_longest_sequence,cur_length)

    return current_longest_sequence
    
nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
nums = [0,3,7,2,5,8,4,6,0,1]

print(longestConsecutive(nums))
nums = [1,0,1,2]
print(longestConsecutive(nums))