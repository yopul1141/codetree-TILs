n, k = map(int, input().split())
arr = [
    list(input().split())
    for _ in range(n)
]
base = [0]*10000
k = k+1

scale = 0
for num, value in arr:
    base[int(num)] = 1 if value == "G" else 2
    scale = max(scale, int(num))

result = 0
for i in range(1, k+1):
    result += base[i]

cur = result
for i in range(2, scale+1):
    cur = cur - base[i-1] + base[i+k-1]
    result = max(result, cur)
print(result)