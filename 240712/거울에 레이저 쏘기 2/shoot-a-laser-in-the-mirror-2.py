n = int(input())
arr = []
for _ in range(n):
    string = input()
    arr.append(list(string))
    
k = int(input())
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

# Determine the initial position and direction
start_direction = (k - 1) // n
dir = (2 + start_direction) % 4

starts = {}
for i in range(4):
    for j in range(1, n + 1):
        tmp = n * i + j
        a, b = 0, 0
        if i == 0:
            a, b = 0, j - 1
        elif i == 1:
            a, b = j - 1, n - 1
        elif i == 2:
            a, b = n - 1, n - j
        else:
            a, b = n - j, 0
        starts[tmp] = (a, b)       

x, y = starts[k]

def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

answer = 0
while True:
    if not is_range(x, y):
        break
    if arr[x][y] == '\\':
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        else:
            dir = 0
    elif arr[x][y] == '/':
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        else:
            dir = 2
    x, y = x + dxs[dir], y + dys[dir]
    answer += 1

print(answer)