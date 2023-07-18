def selection_sort(a):
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


d = [4, 1, 2, 5, 6, 7, 9, 10, 3, 8]
selection_sort(d)
print(d)
