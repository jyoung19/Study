def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    n = len(board)
    danger = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for d in range(8):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = 1
                danger[i][j] = 1  # 지뢰 자체도 위험지역

    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_count += 1
    return safe_count
