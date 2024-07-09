n,a = input().split()
cnt = 0
for i in range(int(n)):
    val = input()
    if val == a:
        cnt += 1
print(cnt)