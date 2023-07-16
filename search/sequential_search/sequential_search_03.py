# 리스트에서 특정 숫자 찾기
# 전체 리스트를 순회하며, 해당하는 index를 반환한다.
def search_list(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
