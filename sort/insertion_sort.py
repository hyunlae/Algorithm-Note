def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [7, 6, 5, 2, 4, 1, 3]
insertion_sort(d)
print(d)
