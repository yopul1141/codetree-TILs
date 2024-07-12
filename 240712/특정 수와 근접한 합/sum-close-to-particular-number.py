import sys

n,s = map(int,input().split())
arr = list(map(int,input().split()))
min_val = sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        if i != j:
            cur = 0
            for k in range(n):
                if k != i and k!= j:
                    cur += arr[k]
            min_val = min(min_val,abs(cur-s))
print(min_val)