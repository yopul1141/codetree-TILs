n = int(input())
white_paint = [0] * 10000
black_paint = [0] * 10000
color = [0] * 10000
cur = 5000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'R':
        for j in range(cur, cur + x):
            black_paint[j] += 1
            color[j] = 2
        cur = cur+x-1
    elif direction == 'L':
        for j in range(cur - x, cur):
            white_paint[j+1] += 1
            color[j+1] = 1
        cur = cur-x+1

white = 0
black = 0
gray = 0

for i in range(len(white_paint)):
    if white_paint[i] >= 2 and black_paint[i] >= 2:
        gray += 1
    else:
        if color[i] == 1:
            white += 1
        elif color[i] == 2:
            black += 1
print(white, black, gray)