# Sum of even & odd elements

def sum_of_evenOdd(arr):
    even_sum = 0
    odd_sum = 0
    
    for num in arr:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
            
    return even_sum, odd_sum


n = int(input())
arr = list(map(int, input().split()))

even, odd = sum_of_evenOdd(arr)

print(even, odd)