sum = 0
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    for j in range(a,b+1):
        if j%2 == 0:
            sum += j
    print(sum)
    sum = 0