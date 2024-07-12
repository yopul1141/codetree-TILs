n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

pattern_count = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            for k in range(8):
                cnt = 0
                for l in range(1, 3):
                    nx, ny = i + dx[k] * l, j + dy[k] * l
                    if in_range(nx, ny) and arr[nx][ny] == 'E':
                        cnt += 1
                    else:
                        break
                if cnt == 2:
                    pattern_count += 1

print(pattern_count)