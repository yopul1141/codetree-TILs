n = int(input())
arr = list(map(int,input().split()))
def plus(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = abs(arr[i])
plus(arr)
for i in arr:
    print(i,end = " ")