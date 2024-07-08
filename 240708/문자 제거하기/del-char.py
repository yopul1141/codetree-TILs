n = input()
for i in range(len(n)-1):
    a = int(input())
    if len(n) > a:
        n = n[:a]+n[a+1:]
    else:
        n = n[:-1]
    print(n)