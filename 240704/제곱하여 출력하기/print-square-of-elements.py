n = int(input())
a = list(map(int,input().split()))
arr = []
for i in a:
    arr.append(i**2)

for i in arr:
    print(i, end=" ")