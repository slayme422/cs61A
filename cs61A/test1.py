def make_withdraw(balance):
    b=[balance]
    def withdraw(amount):
        #nonlocal balance
        if amount>b[0]:
            return '你的余额不足'

        b[0]=b[0]-amount
        return b[0]
    return withdraw

withdraw=make_withdraw(100)


def sequence(f1,f2,sequence):
    """
    add=lambda x:x+1
    triple=lambda x: 3 * x
sequence(add,triple,1211)(1) (add)(triple)(add)(add)
8. # 1->2->3->9->10

    """
    zipper=lambda x : x
    helper=lambda f,g: lambda x:f(g(x))
    while sequence>0:
        if sequence %10==1:
            zipper=helper(f1,zipper)
        else:
            zipper=helper(f2,zipper)

        sequence=sequence //10
    
    return zipper

print(sequence(lambda x:x+1 ,lambda y: y*3,1211)(1))