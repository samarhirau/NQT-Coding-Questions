#  Power of a number (without using built-in)

def power(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    result = 1
    for _ in range(exponent):
        result *= base

    return result


base = float(input().strip())
exponent = int(input().strip())

print(power(base, exponent))