n = int(input())
arr = list(map(int,input().split()))
def max_size(n):
    cur = 0
    for i in range(n):
        if arr[i] > cur:
            cur = arr[i]
    return cur
print(max_size(n))