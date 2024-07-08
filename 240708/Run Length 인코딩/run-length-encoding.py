n = input()
cnt = 0
for i in range(1,len(n)):
    if n[i] != n[i-1]:
        cnt += 1
print((cnt+1)*2)
cnt = 0
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        cnt += 1
        if i == len(n)-1:
            print(n[i - 1], end="")
            print(cnt + 1, end="")
    else:
        print(n[i-1],end="")
        print(cnt+1,end="")
        cnt = 0