import sys

n, k = map(int,input().split())
arr = list(map(int,input().split()))
max_val = -sys.maxsize
for i in range(n - k + 1):
    cur = 0
    for j in range(i, i + k):
        cur += arr[j]

    max_val = max(max_val, cur)

print(max_val)