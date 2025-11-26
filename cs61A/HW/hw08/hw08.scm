(define (ascending? s)
        (if (null? s)
        #t
            (if (null? (cdr s))
                #t
                (if (< (car (cdr s)) (car s))
                    #f
                    (ascending? (cdr s))))))
(define (my-filter pred s)
        (if (null? s)
            nil
            (if (pred (car s))
                (cons (car s) (my-filter pred (cdr s)))
                (my-filter pred (cdr s))
            )))


(define (interleave lst1 lst2)
        (if (null? lst1)
            lst2
            (if (null? lst2)
            lst1
            (cons (car lst1) cons(car lst2)) (interleave (cdr lst1) (cdr lst2)))))

(define (no-repeats s)
    (if (null? s)
         nil
        (cons (car s)
                (no-repeats (filter (lambda (y) (not (= y (car s)))) (cdr s)))))
)


scm> (no-repeats (list 1 2 3 4 5))
(1 2 3 4 5)
scm> (no-repeats (list 1 2 3 5 5))
(1 2 3 5)
scm> (no-repeats (list 3 3 3 5 5))
(3 5)
