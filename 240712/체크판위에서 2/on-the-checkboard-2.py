def simulate(count, r, c, val):
    global answer
    if r == R - 1 and c == C - 1:
        if count == 3:
            answer += 1
        return

    for nrow in range(r + 1, R):
        for ncol in range(c + 1, C):
            if grid[r][c] != grid[nrow][ncol]:
                simulate(count + 1, nrow, ncol, grid[nrow][ncol])

R, C = map(int, input().split())
grid = []
for _ in range(R):
    row = input().split()
    grid.append([0 if cell == 'W' else 1 for cell in row])

answer = 0

simulate(0, 0, 0, grid[0][0])

print(answer)