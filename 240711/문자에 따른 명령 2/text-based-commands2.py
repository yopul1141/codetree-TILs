n = input()
x, y = 0, 0
dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for i in n:
    if i == 'L':
        if dir_num == 3:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 1
        elif dir_num == 1:
            dir_num = 0
        else:
            dir_num = 3
    if i == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x,y)