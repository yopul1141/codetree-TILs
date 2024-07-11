n = int(input())
arr = []
max_val = 1
cnt = 1
for i in range(n):
    a = int(input())
    arr.append(a)
for i in range(1,n):
    if arr[i] > 0 and arr[i-1] > 0 or arr[i] < 0 and arr[i-1] < 0 :
        cnt += 1
        max_val = max(max_val, cnt)
    else:
        cnt = 1
print(max_val)