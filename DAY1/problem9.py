#  Perfect number

def is_perfect(num):
    if num < 1:
        return False
    
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    
    return divisor_sum == num

num = int(input().strip())
if is_perfect(num):
    print("Perfect")
else:    print("Not Perfect")