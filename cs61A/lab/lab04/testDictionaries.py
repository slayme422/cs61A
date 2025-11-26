def last_digit(x):
    return x%10

def last_second_digit(x):
    return x//10%10

def last_two_digit_sum(x):
    return last_digit(x)+last_second_digit(x)

print(last_two_digit_sum(123))