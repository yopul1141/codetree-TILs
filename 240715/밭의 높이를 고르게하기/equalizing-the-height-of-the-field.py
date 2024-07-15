import sys
n,h,t = map(int,input().split())
arr = list(map(int,input().split()))
min_val = sys.maxsize
for i in range(n):
    cnt = 0
    if i+t <= n:
        for j in arr[i:i+h]:
            if j > t:
                j -= 1
                cnt += 1
            elif j < t:
                j += 1
                cnt += 1
        min_val = min(min_val,cnt)
print(min_val)