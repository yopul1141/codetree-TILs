arr = [[0]*2000 for i in range(2000)]
def size_square(a,b,c,d,z):
    for i in range(a, c):
        for j in range(b, d):
            arr[i+1000][j+1000] = z

for i in range(3):
    x1,y1,x2,y2 = map(int,input().split())
    size_square(x1,y1,x2,y2,i+1)
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1 or arr[i][j] == 2:
            cnt += 1
print(cnt)