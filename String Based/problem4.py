# Remove spaces 

def remove_spaces(s):
    return s.replace(" ", "")

s = input().strip()
result = remove_spaces(s)
print(result)