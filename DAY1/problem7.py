#  Check Palindrome number

def is_palindrome(num):
    if num < 0:
        return False
    
    num_str = str(num)
    return num_str == num_str[::-1]


num = int(input().strip())
if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")
    