n = int(input())

arr = []
for _ in range(n):
    arr.append(list(input()))

K = int(input())
direction = 0

for i in range(4):
    if K - n > 0:
        direction += 1
        K -= n

    elif K - n == 0:
        kan = n -1

    else:
        kan = K - 1


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


x, y = 0, 0

if direction == 0:
    x, y = 0, K-1
elif direction == 1:
    x, y = kan, n-1
elif direction == 2:
    x, y = n-1, kan
elif direction == 3:
    x, y = kan, 0

cnt = 1

while True:
    if arr[x][y] == '\\':
        if direction == 0:
            direction = 3
        elif direction == 1:
            direction = 2
        elif direction == 3:
            direction = 0
        elif direction == 2:
            direction = 1

    if arr[x][y] == '/':
        if direction == 0:
            direction = 1
        elif direction == 3:
            direction = 2
        elif direction == 2:
            direction = 3
        elif direction == 1:
            direction = 0

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break

    x, y = nx, ny
    cnt += 1

print(cnt)