n = int(input())
arr = list(map(int,input().split()))

while True:
    fi = arr.index(max(arr))
    if fi == 0:
        print(1)
        break
    else:
        arr = arr[:fi]
        print(fi+1,end = " ")