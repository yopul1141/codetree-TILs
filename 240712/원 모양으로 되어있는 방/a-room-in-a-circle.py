import sys

min_val = sys.maxsize
n = int(input())
arr = [
	int(input())
	for _ in range(n)
]

for i in range(n):
	cur = 0
	for j in range(n):
		dist = (j + n - i) % n
		cur += dist * arr[j]
	
	min_val = min(min_val, cur)

print(min_val)