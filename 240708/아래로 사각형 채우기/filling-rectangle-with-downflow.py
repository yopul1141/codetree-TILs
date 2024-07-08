n = int(input())
num = 1
arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    num = i+1
    for j in range(n):
        arr[j][i] = num
        num += n
        print(arr[j][i], end = " ")
    print()