a,b = map(int,input().split())
val = a+b
val = str(val)
cnt = 0
for i in val:
    if i == '1':
        cnt += 1
print(cnt)