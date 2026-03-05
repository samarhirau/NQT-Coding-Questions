# Sort array (without inbuilt) 

def sort_array(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr


n = int(input())
arr = list(map(int, input().split()))

result = sort_array(arr)

print(*result)