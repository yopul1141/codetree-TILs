a = list(map(int,input().split()))
arr = [0]*10
for i in a:
    if i == 0:
        break
    else:
        if i//10 != 0:
            arr[i//10] += 1
        else:
            continue

for i in range(1,10):
    print(f"{i} - {arr[i]}")