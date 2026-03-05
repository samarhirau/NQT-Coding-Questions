# Find missing number in array 

def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    
    missing_number = total_sum - arr_sum
    return missing_number

n = int(input())
arr = list(map(int, input().split()))
missing_number = find_missing_number(arr, n)
print(missing_number)