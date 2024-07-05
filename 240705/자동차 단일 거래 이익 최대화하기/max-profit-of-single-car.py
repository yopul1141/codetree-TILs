n = int(input())
arr = list(map(int,input().split()))
best = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if j > i:
            if best < arr[j] - arr[i]:
                best = arr[j] - arr[i]
print(best)