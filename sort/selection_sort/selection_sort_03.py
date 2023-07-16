def selection_sort(a):
    n = len(a)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


d = [2, 4, 5, 1, 3]
selection_sort(d)
print(d)
