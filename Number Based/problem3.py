# Check Armstrong number 

def is_armstrong(num):
    if num < 0:
        return False
    
    num_str = str(num)
    num_digits = len(num_str)
    
    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    return armstrong_sum == num


num = int(input().strip())

if is_armstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")