n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

r, c = n // 2, n // 2

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
num = 1
d = 0

for _ in range(n * n):
    arr[r][c] = num
    num += 1

    nr = r + dr[d]
    nc = c + dc[d]

    if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[nr][nc] != 0:
        d = (d + 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    
    r = nr
    c = nc

for i in range(n):
    print(*arr[i])