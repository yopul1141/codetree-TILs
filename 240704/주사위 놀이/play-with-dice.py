a = list(map(int,input().split()))
arr = [0]*10
for i in a:
    arr[i] += 1
for i in range(1,7):
    print(f"{i} - {arr[i]}")