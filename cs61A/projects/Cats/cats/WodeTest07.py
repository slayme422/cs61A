def tree(label ,branches=[]):
    for branch in branches:
       assert is_tree(branch)
    return [label]+list(branches)

def branches(t):
    return t[1:]

def label(t):
    return t[0]

def is_tree(tree):
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        print(branch)
        if not is_tree(branch):
            return False
        
    return True     

def is_leaf(tree):
    return not branches(tree)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(tree)])

tree_list=[3,[1,[0],[1]],[2,[1],[1,[0],[1]]]]
def print_tree(tree_list,indent=0):
    print(' '* indent+str(label(tree_list)))
    for branch in branches(tree_list):
        print_tree(branch,indent+1)
print_tree(tree_list)

haste=tree('h',[tree('a'), [tree('s'),
                            tree('t')],
                            tree('e')])

def print_sums(t, so_far):
    so_far=so_far+label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far) 

