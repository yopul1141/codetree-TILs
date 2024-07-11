n = int(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for i in range(n):
    direct, dis = input().split()
    dis = int(dis)
    if direct == 'E':
        x, y = x + dx[0] * dis, y + dy[0] * dis
    elif direct == 'S':
        x, y = x + dx[1] * dis, y + dy[1] * dis
    elif direct == 'W':
        x, y = x + dx[2] * dis, y + dy[2] * dis
    elif direct == 'N':
        x, y = x + dx[3] * dis, y + dy[3] * dis
print(x, y)