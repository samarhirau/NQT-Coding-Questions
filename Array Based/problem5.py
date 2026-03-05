# Find frequency of elements 

def frequency(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    for key in freq:
        print(key, freq[key])


n = int(input())
arr = list(map(int, input().split()))

frequency(arr)