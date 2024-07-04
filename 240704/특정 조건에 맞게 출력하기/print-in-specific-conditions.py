a = list(map(int, input().split()))
arr = []
for i in a:
    if i == 0:
        break
    else:
        if i%2 == 0:
            arr.append(i//2)
        else:
            arr.append(i+3)
for i in arr:
    print(i,end=" ")