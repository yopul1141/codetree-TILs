n = int(input())
x = 'A'
cnt = 0
for i in range(n):
    for j in range(i+1):
        print(chr(ord(x)+cnt), end="")
        cnt += 1
        if cnt == 26:
            cnt = 0
    print()