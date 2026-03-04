# Fibonacci series (nth term or print series)


def fibonacci(n):
    if n < 0:
        return None
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a


n = int(input().strip())
result = fibonacci(n)

if result is None:
    print("Invalid Input")
else:
    print(result)