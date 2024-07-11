n = int(input())
arr = [0] * 1000
cur = 500
cnt = 0
for i in range(n):
    x,direct = input().split()
    if direct == 'R':
        for j in range(cur,cur+int(x)):
            arr[j] += 1
        cur = cur+int(x)
    if direct == 'L':
        for j in range(cur-int(x),cur):
            arr[j] += 1
        cur = cur-int(x)
for i in range(len(arr)):
    if arr[i] > 1:
        cnt += 1
print(cnt)