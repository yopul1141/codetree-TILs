def simulate(count, r, c, val):
    global answer
    if r == R - 1 and c == C - 1:
        if count == 3:
            answer += 1
        return

    for i in range(r + 1, R):
        for j in range(c + 1, C):
            if arr[r][c] != arr[i][j]:
                simulate(count + 1, i, j, arr[i][j])

R, C = map(int, input().split())
arr = []
for _ in range(R):
    row = input().split()
    arr.append([0 if cell == 'W' else 1 for cell in row])

answer = 0

simulate(0, 0, 0, arr[0][0])

print(answer)