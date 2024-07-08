n, m = map(int, input().split())
array = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    array[a-1][b-1] = a*b
for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print()