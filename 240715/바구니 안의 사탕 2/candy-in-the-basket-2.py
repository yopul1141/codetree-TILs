n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
basket = [0] * 101

for i in range(n):
    value, position = arr[i]
    basket[position] = value

max_val = 0
for i in range(1, 101):
    if i - k - 1 >= 0 and i + k <= 100:
        sum_val = 0
        for j in range(i - k, i + k + 1):
            sum_val += basket[j]
        max_val = max(max_val, sum_val)

print(max_val)