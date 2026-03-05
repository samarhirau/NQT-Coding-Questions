# Remove duplicates

def remove_duplicates(arr):
    unique = []
    seen = set()
    
    for num in arr:
        if num not in seen:
            unique.append(num)
            seen.add(num)
            
    return unique


n = int(input().strip())
arr = list(map(int, input().split()))

print(remove_duplicates(arr))