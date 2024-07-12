n, m = map(int, input().split())
arr = [  
    [0 for _ in range(m)]
    for _ in range(n)
]

r, c, d = 0, 0, 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
num = 65
for _ in range(n * m):
    arr[r][c] = chr(num)
    nr = r + dr[d]
    nc = c + dc[d]

    if nr < 0 or nr >= n or nc < 0 or nc >= m or \
            arr[nr][nc] != 0:
        d = (d + 1) % 4
    
    r = r + dr[d]
    c = c + dc[d]
    num += 1
    if num == 91:
        num = 65

for i in range(n):
    print(*arr[i])