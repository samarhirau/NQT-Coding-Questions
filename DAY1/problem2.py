# Print Prime numbers in range

def print_prime(n):
    if n > 2:
        print(2, end=" ")
    
    for i in range(3, n, 2):
        is_prime = True
        for j in range(3, int(i**0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")

n = int(input().strip())
print_prime(n)
        