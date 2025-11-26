identity=lambda x: x
square=lambda x: x * x
triple=lambda x: x * 3

def interleaved_sum(n, odd_func, even_func):
    #从1开始往上加
    def helper(k , isOdd):
        if k >n:    
            return 0
        elif isOdd:
            return odd_func(k)+ helper(k+1,False)
        else:
            return even_func(k)+helper(k+1,True)
    return helper(1,True)    

print(interleaved_sum(1,square,triple))
print(interleaved_sum(0,square,triple))
print(interleaved_sum(5,square,triple))