n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
print(max_val, end=" ")
arr.remove(max_val)
print(max(arr))