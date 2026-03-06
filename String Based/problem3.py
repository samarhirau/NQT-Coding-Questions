# Reverse a string

def reverse_string(s):
    return s[::-1]

s = input().strip()
reversed_s = reverse_string(s)

print(reversed_s)