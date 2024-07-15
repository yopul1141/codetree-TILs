n,k = map(int, input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
basket = [0]* 100
max_val = 0
for i in range(n):
    basket[arr[i][1]-1] = arr[i][0]
for i in range(100):
    if i-k-1 >= 0 and i+k+1 <= 100:
        sum_val = 0
        for j in range(i-k-1,i+k+1):
            sum_val += basket[j]
        max_val = max(max_val,sum_val)
print(max_val)