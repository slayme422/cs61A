(define (curry-cook formals body)
  (if (null? (cdr formals))
      `(lambda (,(car formals)) ,body)       ; 插入 (car formals) 和 body
      `(lambda (,(car formals)) ,(curry-cook (cdr formals) body))))  ; 递归插入

(define (curry-consume curry args)
  (if (null? args)
  curry
  (curry-consume (curry (car args))(cdr args))))


(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons _________
        (map (lambda (option)
               (cons _______________ (cdr option)))
             (car (cdr (cdr switch-expr))))))
