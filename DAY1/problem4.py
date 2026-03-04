# Factorial of number

def factorial(n):
    if n < 0:
        return None
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


num = int(input().strip())
result = factorial(num)


print(result)