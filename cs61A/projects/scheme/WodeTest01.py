"""
Tree(1,[Tree(2,[Tree(3)])])"""
class Tree():
    def __init__(self,label,branches=[]):
        self.label=label
        self.branches=branches
    def is_leaf(self):
        if self.branches: #不空的时候是 如果self.branches有东西，那返回False self.branches是空的话->判断为False返回叶子
            return False
        else:
            return True

arr=[1,5,3] 
print(sorted(arr))