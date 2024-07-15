from itertools import permutations

# 입력 받기
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

# 리스트 a의 각 위치에서 부분 리스트 비교
for i in range(n - m + 1):
    for perm in permutations(b):
        if a[i:i + m] == list(perm):
            cnt += 1
            break  # 일치하는 부분 리스트를 찾으면 더 이상의 비교는 불필요

print(cnt)