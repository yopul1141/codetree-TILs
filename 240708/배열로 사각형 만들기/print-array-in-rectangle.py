n = 5
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for j in range(n):
    arr_2d[0][j] = 1

for i in range(1, n):
    for j in range(n):
        if j == 0:
            arr_2d[i][j] = 1
        else:
            arr_2d[i][j] = arr_2d[i][j-1] + arr_2d[i-1][j]

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()