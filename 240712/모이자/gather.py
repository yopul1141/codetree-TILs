n = int(input())
arr = list(map(int,input().split()))
result = []

for i in range(n):
    cur = 0
    for j in range(n):
        if j != i:
            cur += arr[j] * abs(j - i)
    result.append(cur)
print(min(result))