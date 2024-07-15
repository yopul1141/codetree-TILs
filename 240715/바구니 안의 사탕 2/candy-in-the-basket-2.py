n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
basket = [0] * 101

for i in range(n):
    value, position = arr[i]
    basket[position] = value

max_val = 0

for i in range(101):
    sum_val = 0
    for j in range(max(0, i - k), min(101, i + k + 1)):
        sum_val += basket[j]
    max_val = max(max_val, sum_val)

print(max_val)