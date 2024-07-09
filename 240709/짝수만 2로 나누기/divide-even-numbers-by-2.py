n = int(input())
arr = list(map(int,input().split()))
def edit_list(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            arr[i] = arr[i]//2
edit_list(arr)
for i in arr:
    print(i,end =" ")