import sys
n = int(input())
arr = list(map(int,input().split()))
min_val = sys.maxsize
for i in arr:
    if i < min_val:
        min_val = i
cnt = arr.count(min_val)
print(min_val,cnt)