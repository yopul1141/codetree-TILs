n,k = map(int,input().split())
arr = [0]*n
def clean(a,b):
    for i in range(a,b+1):
        arr[i-1] += 1
for i in range(k):
    a,b = map(int,input().split())
    clean(a,b)

print(max(arr))