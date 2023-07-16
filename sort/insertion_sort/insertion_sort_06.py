# 삽입 정렬 알고리즘
# 첫번째 index를 key 로 설정하고, index - 1 과 비교하여 더 작은 값이 나올 때까지 확인한다.
# 더 작은값이 없으면, key를 삽입한다.

def insertion_sort(a):
    for i in range(len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [7, 6, 5, 2, 4, 1, 3]
insertion_sort(d)
print(d)
