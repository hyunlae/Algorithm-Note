# 리스트에서 특정 숫자 찾기

def search_list(a, x):
    n = len(a)
    for i in range(n):
        if x == a[i]:
            return i
    return -1


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
