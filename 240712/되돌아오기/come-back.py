n = int(input())
x, y = 0,0
time = 0
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'N': 0,
    'E': 1,
    'W': 2,
    'S': 3
}

def find_time(n):
    global x,y,time
    for i in range(n):
        direct, dis = input().split()
        dir_num = mapper[direct]
        for j in range(int(dis)):
            x, y = x + dxs[dir_num], y + dys[dir_num]
            time += 1
            if x == 0 and y == 0:
                return time
    if x != 0 and y != 0:
        return -1
print(find_time(n))