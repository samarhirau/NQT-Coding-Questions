#  Remove duplicate characters

def remove_duplicates(s):
    seen = set()
    result = []
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

s = input().strip()
result = remove_duplicates(s)
print(result)