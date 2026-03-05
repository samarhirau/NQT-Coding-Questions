# LCM & HCF

def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return abs(x * y) // hcf(x, y)


num1 = int(input().strip())
num2 = int(input().strip())

print(hcf(num1, num2))
print(lcm(num1, num2))