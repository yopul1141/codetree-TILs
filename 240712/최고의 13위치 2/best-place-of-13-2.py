n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0

for i in range(n):
    for j in range(n - 2):
        sum1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        for k in range(i, n):
            for l in range(n - 2):
                if i == k and l < j + 3:
                    continue
                sum2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, sum1 + sum2)

print(max_cnt)