# Check if substring exists 
def substring_exists(s, sub):
    n = len(s)
    m = len(sub)

    for i in range(n - m + 1):
        if s[i:i+m] == sub:
            return True

    return False


s = input().strip()
sub = input().strip()

if substring_exists(s, sub):
    print("Yes")
else:
    print("No")