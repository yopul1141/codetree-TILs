n = int(input())
arr = [[0]*200 for i in range(200)]
def size_square(a,b):
    for i in range(a, a+8):
        for j in range(b, b+8):
            arr[i+100][j+100] = 1

for i in range(n):
    a,b = map(int,input().split())
    size_square(a,b)
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)