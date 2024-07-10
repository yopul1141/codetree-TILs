n = int(input())
arr = list(map(int,input().split()))
for i in range(n):
    if i%2 == 0:
        a = arr[:i+1]
        a.sort()
        print(a[i//2],end = " ")