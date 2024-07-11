n,t = map(int,input().split())
r,c,d = input().split()
x, y = int(r), int(c)

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

dir_num = mapper[d]
nx, ny = x + dxs[dir_num], y + dys[dir_num]

def in_range(x, y):
    return 0 < x and x < n and 0 < y and y < n

while t>0:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num # change direction
        t -= 1
    else:
        # move
        x, y = x + dxs[dir_num], y + dys[dir_num]
        t -= 1
print(x,y)