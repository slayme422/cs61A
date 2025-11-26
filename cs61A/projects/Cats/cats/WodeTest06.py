#访问3下面的1下面的0

tree_list=[3,[1,[0],[1]],[2,[1],[1,[0],[1]]]]

print(tree_list[1][1])
print(tree_list[1][1][0])
print(type(42))
print(type([1,2,3]))
print(type(((1),(2),(3)))) #tuple
print(type({'1':1, 'player_id': "jake"}))

def tree(label,branches=[]):
    for branch in branches:
        assert(is_tree(branch))
    return [label]+list(branches)

#根部
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(t):
    if type(t)==list or len(tree)<1:
        return False

    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True



def closest_to_number(target,arrays=[]):
    current_lowest_difference=float('inf')
    current_lowest_number=float('inf')
    for array_num in arrays:
        difference=abs(array_num-target)
        if difference<=5 and difference<current_lowest_difference:
            current_lowest_difference=difference
            current_lowest_number=array_num
    if current_lowest_number==float('inf'):
        return None
    return  current_lowest_number

arrays=[1,300,50,75,99]
print(f'数组中最接近79并且在5里面的的是'+str(closest_to_number(81,arrays)))

print(max([5,3,9,4],key=lambda a:abs(a*a-24)))
      

    