import sys
arr = list(map(int,input().split()))
min_val = sys.maxsize
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            total_1 = arr[i] + arr[j] + arr[k]
            total_2 = sum(arr) - total_1
            res = abs(total_1 - total_2)
            min_val = min(min_val, res)

print(min_val)