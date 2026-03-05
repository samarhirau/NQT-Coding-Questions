#  Merge two arrays

def merge_arrays(arr1, arr2):
    return arr1 + arr2


n1 = int(input())
arr1 = list(map(int, input().split()))

n2 = int(input())
arr2 = list(map(int, input().split()))

merged = merge_arrays(arr1, arr2)

print(*merged)