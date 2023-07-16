def binary_search(a, x):
    a.sort()
    n = len(a)

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(binary_search(v, 18))
print(binary_search(v, 33))
print(binary_search(v, 900))
