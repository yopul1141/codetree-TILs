n = int(input())
prod = 1
for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        prod *= j
    print(prod)
    prod = 1