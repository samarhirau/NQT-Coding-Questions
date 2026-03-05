#  Perfect number

def is_perfect(num):
    if num <= 1:
        return False
    
    total_sum = 0
    
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            total_sum += i
            
    return total_sum == num


num = int(input().strip())

if is_perfect(num):
    print("Perfect")
else:
    print("Not Perfect")