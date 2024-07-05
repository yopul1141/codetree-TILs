arr = list(map(int,input().split()))
low = []
high = []
for i in arr:
    if i < 500:
        low.append(i)
    else:
        high.append(i)
print(max(low), min(high))