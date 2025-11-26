(define (over-or-under num1 num2)
(if (< num1 num2)
-1
(if (= num1 num2)
0
1)))

(define (make-adder num)
  (define (adder x)
    (+ num x))
    adder)

(define (composed f g) (lambda (x) (f(g x))))
#n是让f重复的次数 
(define (repeat f n)
f
(if(> n 0)
(f(lambda (x)(f(repeat f (- n 1))x)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
 (if(= 0 b)
  a
  (gcd b (modulo a b))))
