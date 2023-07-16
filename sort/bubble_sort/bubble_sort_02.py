# 버블정렬

def bubble_sort(a):
    n = len(a)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


d = [7, 6, 5, 2, 4, 1, 3]
bubble_sort(d)
print(d)
