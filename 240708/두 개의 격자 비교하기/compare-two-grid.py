n,m = map(int,input().split())
arr_1 = []
arr_2 = []
for i in range(n):
    arr_1.append(list(map(int,input().split())))
for i in range(n):
    arr_2.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()