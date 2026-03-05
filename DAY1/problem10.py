# . Reverse a number

def reverse_num(num):
    if num == 0:
        return 0
    elif num < 0:
        sign = -1
      
        
    num = abs(num)
    
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
        
    return sign * rev


num = int(input().strip())
print(reverse_num(num))