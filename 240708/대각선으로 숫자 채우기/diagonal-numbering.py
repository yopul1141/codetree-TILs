n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
num = 1
    
for diag in range(n + m - 1):
    if diag < m:
        start_row, start_col = 0, diag
    else:
        start_row, start_col = diag - m + 1, m - 1
    
    while start_row < n and start_col >= 0:
        arr[start_row][start_col] = num
        num += 1
        start_row += 1
        start_col -= 1
for row in arr:
    print(" ".join(map(str, row)))