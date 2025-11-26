square=lambda x: x*x

def pow(x,y):
    if y==1:
        return x
    if y%2==1:#奇数
        return x* square(pow(x,y//2))
    else:
        return square(pow(x,y//2))
(define (pow x y)
 (if (= y 1)
  x
  (if (even? y)
       (square(pow x (quotient y 2)))
       (* x (square(pow x (quotient y 2)))))))