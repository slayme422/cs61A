add=lambda x:x+2
square=lambda x:x*x
nothing=lambda x:x
Operators={"+":add,"**":square,"Nope":nothing}
def cal_eval(expression):
    Operator=expression[0]
    args=expression[1:]
    return apply_func(Operators[Operator],args)
def apply_func(f,nums):
    for num in nums:
        f(num)
    
    
exp=["+",1,2,3]

print(0 is False)
print(0 == False)