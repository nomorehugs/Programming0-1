# used joker
def last(items):
    return items[len(items) - 1]

def before_last(items):
    return items[len(items) - 2]

def fib(n):
    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]
    
    result = [1, 1]
    
    while len(result) < n:
        next_fib = last(result) + before_last(result)
        result = result + [next_fib]

    return result

def count_digits(n):
    result = 0

    while n != 0:
        result += 1
        n = n // 10

    return result

def to_number(numbers):
    result = 0

    for number in numbers:
        multi = 10 ** count_digits(number)
        result = result * multi + number 
    
    return result

def fib_number(n):
    return to_number(fib(n))

print(fib_number(3))
print(fib_number(8))
