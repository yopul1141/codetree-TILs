n = int(input())
arr = [1,n]
i = 0
while True:
    arr.append(arr[i] + arr[i+1])
    if arr[i] + arr[i+1] > 100:
        break
    i += 1

for j in arr:
    print(j, end = " ")