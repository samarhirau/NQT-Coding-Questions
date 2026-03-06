# Find frequency of characters in a string

def char_frequency(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    return freq


s = input().strip()
frequency = char_frequency(s)

for char, count in frequency.items():
    print(char, count)