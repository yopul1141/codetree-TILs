n = int(input())
arr = []
arr_cnt = []
cnt = 1
for i in range(n):
    a = int(input())
    arr.append(a)
for i in range(1,len(arr)):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        arr_cnt.append(cnt)
        cnt = 1
print(max(arr_cnt))