def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


v = [7, 9, 17, 18, 33, 33, 42, 58, 92, 100, 178, 234, 452, 845, 1848, 1934]
print(binary_search(v, 9))
print(binary_search(v, 33))
print(binary_search(v, 845))
