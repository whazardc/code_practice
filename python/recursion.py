# 3! = 3 * 2 * 1

def factorial(n):
    if n == 1:  # base case
        return 1    
    return n* factorial(n-1)    # recursive case, function is called within itself

print(factorial(5))