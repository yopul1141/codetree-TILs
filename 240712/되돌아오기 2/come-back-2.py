n = input()
x, y = 0,0
time = 0
dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
def find_time(n):
    global x,y,time,dir_num
    for i in n:
        if i == 'L':
            time += 1
            if dir_num == 3:
                dir_num = 2
            elif dir_num == 2:
                dir_num = 1
            elif dir_num == 1:
                dir_num = 0
            else:
                dir_num = 3
        if i == 'R':
            time += 1
            if dir_num == 0:
                dir_num = 1
            elif dir_num == 1:
                dir_num = 2
            elif dir_num == 2:
                dir_num = 3
            else:
                dir_num = 0
        if i == 'F':
            time += 1
            x, y = x + dx[dir_num], y + dy[dir_num]
            if x == 0 and y == 0:
                return time
    if x != 0 and y != 0:
        return -1
print(find_time(n))