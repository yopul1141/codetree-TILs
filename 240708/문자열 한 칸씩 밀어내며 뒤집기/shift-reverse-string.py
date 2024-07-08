n,q = input().split()
s = ""
for i in range(int(q)):
    a = int(input())
    if a == 1:
        n = n[1:]+n[0]
        print(n)
    elif a == 2:
        n = n[-1]+n[:-1]
        print(n)
    elif a == 3:
        for j in n[::-1]:
            s += j
        n = s
        s = ""
        print(n)