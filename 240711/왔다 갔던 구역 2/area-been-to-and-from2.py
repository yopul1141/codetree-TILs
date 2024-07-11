n = int(input())
arr = [0] * 100
cur = 50
cnt = 0
for i in range(n):
    x,direct = input().split()
    if direct == 'R':
        for j in range(cur,cur+int(x)+1):
            arr[j] += 1
            cur = cur+int(x)+1
    if direct == 'L':
        for j in range(cur-int(x),cur+1):
            arr[j] += 1
            cur = cur-int(x)
for i in range(len(arr)):
    if arr[i] > 1:
        cnt += 1
print(cnt)