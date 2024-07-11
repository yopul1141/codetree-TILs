n = int(input())
arr = [0] * 100
cur = 50
cnt = 0
for i in range(n):
    x,direct = input().split()
    if direct == 'R':
        for j in range(cur,cur+int(x)):
            arr[j] += 1
        cur = cur+int(x)
    elif direct == 'L':
        for j in range(cur-int(x),cur):
            arr[j] += 1
        cur = cur-int(x)
cnt = sum(1 for i in arr if i > 1)
print(cnt)