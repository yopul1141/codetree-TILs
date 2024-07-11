n = int(input())
arr = [[0]*200 for i in range(200)]
def size_square(a,b,c,d):
    for i in range(a, c):
        for j in range(b, d):
            arr[i+100][j+100] = 1

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    size_square(x1,y1,x2,y2)
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)