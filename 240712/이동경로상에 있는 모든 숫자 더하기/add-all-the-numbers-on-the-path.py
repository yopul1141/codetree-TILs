n,t = map(int,input().split())
s = input()
arr = []
for i in range(n):
    a = list(map(int,input().split()))
    arr.append(a)

x, y = n//2, n//2  

def in_range(x,y): 
    return 0 <= x < n and 0 <= y < n 

cur = arr[x][y]
dir_num = 0 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in s:  
    if i == "L": 
        dir_num = (dir_num+3)%4
    elif i == "R": 
        dir_num = (dir_num+1)%4
    else:
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx,ny): 
            cur += arr[nx][ny]
            x, y = nx, ny

print(cur)