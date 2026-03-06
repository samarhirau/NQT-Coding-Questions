# Anagram check

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


    
s1 = input().replace(" ", "").lower()
s2 = input().replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")