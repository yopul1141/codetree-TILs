def check_winner(board):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                player = board[i][j]
                for dx, dy in directions:
                    count = 0
                    for k in range(5):
                        nx, ny = i + k * dx, j + k * dy
                        if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == player:
                            count += 1
                        else:
                            break
                    if count == 5:
                        if 0 <= i - dx < 19 and 0 <= j - dy < 19 and board[i - dx][j - dy] == player:
                            continue
                        if 0 <= i + 5 * dx < 19 and 0 <= j + 5 * dy < 19 and board[i + 5 * dx][j + 5 * dy] == player:
                            continue
                        mid_x, mid_y = i + 2 * dx + 1, j + 2 * dy + 1
                        return player, mid_x, mid_y
    return 0, 0, 0

arr = [list(map(int, input().split())) for _ in range(19)]
winner, x, y = check_winner(arr)

if winner:
    print(winner)
    print(x, y)
else:
    print(0)