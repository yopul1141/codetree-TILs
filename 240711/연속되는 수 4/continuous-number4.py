n = int(input())
arr = []
max_val = 1
cnt = 1
for i in range(n):
    a = int(input())
    arr.append(a)
for i in range(1,n):
    if arr[i] > arr[i-1]:
        cnt += 1
        max_val = max(max_val, cnt)
    else:
        cnt = 1
print(max_val)