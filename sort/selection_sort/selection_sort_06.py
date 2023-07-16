# 선택정렬 알고리즘
# 정렬되지 않은 리스트에서 가장 작은수를 맨앞으로 빼낸다.

def selection_sort(a):
    for i in range(len(a) - 1):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


d = [10, 2, 4, 5, 6, 1, 3]
selection_sort(d)
print(d)
