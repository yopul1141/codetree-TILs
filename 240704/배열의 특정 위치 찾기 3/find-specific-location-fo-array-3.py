a = list(map(int,input().split()))
val = 0
cnt = 0
for i in a:
    if i == 0:
        if cnt >= 3:
            val = sum(a[cnt-3:cnt])
        else:
            val = sum(a[0:cnt])
        break
    cnt += 1
print(val)