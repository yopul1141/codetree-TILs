# 입력 받기
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 리스트 b를 정렬
b_sorted = sorted(b)
cnt = 0

# 리스트 a의 각 위치에서 부분 리스트를 정렬하여 비교
for i in range(n - m + 1):
    if sorted(a[i:i + m]) == b_sorted:
        cnt += 1

print(cnt)