# Find largest and smallest

def find_largest_smallest(arr):
    if len(arr) == 0:
        return None, None

    largest = smallest = arr[0]

    for num in arr[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


n = int(input().strip())
arr = list(map(int, input().split()))

largest, smallest = find_largest_smallest(arr)

print(largest, smallest)