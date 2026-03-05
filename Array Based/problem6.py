n = int(input())
arr = list(map(int, input().split()))
d = int(input())

d = d % n

result = arr[d:] + arr[:d]

for i in result:
    print(i, end=" ")
    
    
n = int(input())
arr = list(map(int, input().split()))
d = int(input())

d = d % n

result = arr[-d:] + arr[:-d]

for i in result:
    print(i, end=" ")