n = int(input())
arr = list(map(int,input().split()))
arr.sort()
a = []
b = []
max_sum = -1
for i in range(n):
    cur = arr[i] + arr[-(i+1)]
    max_sum = max(max_sum,cur)
print(max_sum)