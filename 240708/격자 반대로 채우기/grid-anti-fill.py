n = int(input())
matrix = [[0] * n for _ in range(n)]
num = 1
direction = 1
for col in range(n-1, -1, -1):
    if direction == 1:
        for row in range(n-1, -1, -1):
            matrix[row][col] = num
            num += 1
    else:
        for row in range(n):
            matrix[row][col] = num
            num += 1
    direction *= -1
for row in matrix:
    print(" ".join(map(str, row)))