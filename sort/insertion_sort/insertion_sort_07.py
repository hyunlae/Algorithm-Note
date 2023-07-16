def insertion_sort(a):
    for i in range(len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [10, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(d)
print(d)
