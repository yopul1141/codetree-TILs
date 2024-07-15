n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for i in range(n - m + 1):
    if a[i:i + m] == b:
        cnt += 1

print(cnt)