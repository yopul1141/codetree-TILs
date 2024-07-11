n = int(input())
arr = [0] * 10000
cur = 5000
white = 0
black = 0
for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'R':
        for j in range(cur, cur + x):
            arr[j] = 2
        cur = cur+x-1
    elif direction == 'L':
        for j in range(cur - x, cur):
            arr[j+1] = 1
        cur = cur-x+1

for i in range(len(arr)):
    if arr[i] == 1:
        white += 1
    elif arr[i] == 2:
        black += 1
print(white, black)