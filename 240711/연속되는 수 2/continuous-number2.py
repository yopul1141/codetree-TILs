n = int(input())
arr = []
arr_cnt = []
cnt = 1
for i in range(n):
    a = int(input())
    arr.append(a)
if n == 1:
    arr_cnt.append((cnt))
for i in range(n):
    if arr[i] == arr[i-1]:
        cnt += 1
        if i == len(arr)-1:
            arr_cnt.append((cnt))
    else:
        arr_cnt.append(cnt)
        cnt = 1
print(max(arr_cnt))