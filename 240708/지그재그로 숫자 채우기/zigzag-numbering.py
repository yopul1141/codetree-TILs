n, m = map(int, input().split())
arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] = j * n + i
    else:
        for i in range(n):
            arr[i][j] = j * n + (n - 1 - i)

for row in arr:
    print(" ".join(map(str, row)))