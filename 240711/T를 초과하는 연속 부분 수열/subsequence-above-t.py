n,t = map(int,input().split())
arr = list(map(int,input().split()))
max_val = 0
cnt = 0
for i in range(1,n):
    if arr[i] > t:
        cnt += 1
        max_val = max(max_val, cnt)
    else:
        cnt = 0
print(max_val)