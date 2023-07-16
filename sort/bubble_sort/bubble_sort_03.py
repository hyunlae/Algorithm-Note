# 버블정렬
# n과 n-1 요소를 비교하여 위치를 바꾼다.
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]


d = [19, 39, 34, 45, 28, 11, 9, 50]
bubble_sort(d)
print(d)
