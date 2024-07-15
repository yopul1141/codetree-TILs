n,m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
for i in range(n):
    pos = 0
    for j in b:
        if j in a[i:i+m]:
            if i+m > n:
                break
            pos += 1
            if pos == m:
                cnt += 1
print(cnt)