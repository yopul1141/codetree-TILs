n = int(input())
arr = list(map(int,input().split()))
cnt = n**3
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(i - arr[0]) > 2 and abs(j - arr[1]) > 2 and abs(k - arr[2]) > 2:
                cnt -= 1

print(cnt)