n = int(input())
a = list(map(int,input().split()))
arr = []
for i in a:
    if i%2 == 0:
        arr.append(i)
for i in arr:
    print(i, end = " ")