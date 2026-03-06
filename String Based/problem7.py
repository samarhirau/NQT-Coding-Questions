# Convert lowercase to uppercase (without built-in) 

def to_uppercase(s):
    res = ""
    for c in s:
        if 'a' <= c <= 'z':
            res += chr(ord(c) - 32)
        else:
            res += c
    return res


s = input().strip()
print(to_uppercase(s))
