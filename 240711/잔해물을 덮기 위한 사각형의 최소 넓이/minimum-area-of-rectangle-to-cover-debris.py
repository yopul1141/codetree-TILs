arr = [[0]*2000 for i in range(2000)]
def size_square(a,b,c,d,z):
    for i in range(a, c):
        for j in range(b, d):
            arr[i+1000][j+1000] = z

for i in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    size_square(x1,y1,x2,y2,i+1)

x = []
y = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            x.append(i)
            y.append(j)
print((abs(max(x))-abs(min(x))+1)*(abs(max(y))-abs(min(y))+1))