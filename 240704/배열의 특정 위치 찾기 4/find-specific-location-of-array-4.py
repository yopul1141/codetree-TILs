cnt = 0
val = 0
a = list(map(int,input().split()))
for i in a:
    if i !=0:
        if i%2 == 0:
            val += i
            cnt += 1
    else:
        break
print(cnt, val)