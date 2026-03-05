#  Sum of digits 

def sum_of_digit(num):
    num = abs(num)
    digit_sum = 0
    
    while num > 0:
        digit_sum += num % 10
        num //= 10
        
    return digit_sum


num = int(input().strip())
print(sum_of_digit(num))