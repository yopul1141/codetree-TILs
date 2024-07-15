n = int(input())
arr = list(map(int,input().split()))
cnt = 0
max_sum = 0
for i in range(n):
    for j in range(i, n):
        sum_val = 0
        per = 0
        for k in range(i, j + 1):
            sum_val += arr[k]
            per += 1
        if sum_val/per in arr[i:j+1]:
            cnt += 1
print(cnt)