a = list(map(int, input().split()))
arr = [0]*11
for i in a:
    if i//10 != 0:
        arr[i//10] += 1
    else:
        continue
for i in range(10,0,-1):
    print(f"{i}0 - {arr[i]}")