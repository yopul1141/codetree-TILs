n = input()
cnt = 0
for i in range(1,len(n)):
    if n[i] != n[i-1]:
        cnt += 1
new_len = (cnt+1)*2
print(new_len)
cnt = 0
new = ""
for i in range(1,len(n)):
    if n[i] == n[i-1]:
        cnt += 1
        if i == len(n)-1:
            print(n[i - 1], end="")
            print(cnt + 1, end="")
            new += n[i - 1] + str(cnt + 1)
    else:
        print(n[i-1],end="")
        print(cnt+1,end="")
        new += n[i - 1] + str(cnt + 1)
        cnt = 0
if new_len != len(new):
    print(n[-1],end="")
    print(1)