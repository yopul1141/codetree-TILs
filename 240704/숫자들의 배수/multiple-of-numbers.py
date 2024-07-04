n = int(input())
i = 1
cnt = 0
while True:
    print(n*i, end = " ")
    if (n*i)%5 == 0:
        cnt += 1
        if cnt == 2:
            break
    i += 1