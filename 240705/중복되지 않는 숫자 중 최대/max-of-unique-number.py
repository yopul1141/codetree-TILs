n = int(input())
arr = list(map(int,input().split()))
flag = True
max_val = arr[0]
while flag:
    for i in arr[1:]:
        if i == max_val:
            arr.remove(i)
            max_val = max(arr)
        else:
            flag = False
print(max(arr))