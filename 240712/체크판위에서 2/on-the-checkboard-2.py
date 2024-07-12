r, c = map(int, input().split())
arr = [list(map(str, input().split())) for _ in range(r)]

max_cnt = 0

for i in range(1, r - 1): # 세로
    for j in range(1, c- 1): # 가로
        cycle = 0
        for k in range(i+1, r-1) :
            for l in range(j+1, c-1) :
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[r-1][c-1] :
                    if cycle == 2 :
                        break
                    max_cnt += 1
                    cycle += 1

print(max_cnt)