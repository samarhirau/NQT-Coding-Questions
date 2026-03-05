# find strong number or not

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_strong(num):
    temp = num
    digit_sum = 0
    
    for digit in str(num):
        digit_sum += factorial(int(digit))
    
    return digit_sum == temp


num = int(input().strip())

if is_strong(num):
    print("Strong")
else:
    print("Not Strong")