a = list(map(int,input().split()))
cnt = 0
for i in a:
    if i%3 == 0:
        print(a[cnt-1])
        break
    else:
        cnt += 1