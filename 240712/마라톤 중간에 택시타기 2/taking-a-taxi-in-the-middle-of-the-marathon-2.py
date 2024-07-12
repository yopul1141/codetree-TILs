import sys
min_val = sys.maxsize

n = int(input())
arr = [
	list(map(int, input().split()))
	for _ in range(n)
]

for i in range(1, n - 1):
	cur = 0
	prev_idx = 0
	for j in range(1, n):
		if j == i:
			continue
		cur += abs(arr[j][0] - arr[prev_idx][0]) + abs(arr[j][1] - arr[prev_idx][1])
		prev_idx = j
	
	min_val = min(min_val, cur)

print(min_val)