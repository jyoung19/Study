def solution(n):
    # 빈 리스트 만들기
    spiral = [[0] * n for _ in range(n)]
    
    # 무언가에 부딪혔을 때 [우, 하, 상, 좌] 순서로 움직이게 하는 방향 설정
    # [오른쪽으로 이동, 부딪히면 아래로 이동, 부딪히면 왼쪽으로 이동, 부딪히면 위로 이동] 반복
    dx = [1,0,-1,0]  # 처음 방향은 오른쪽이니 dx=1, dy=0
    dy = [0,1,0,-1]  # 부딪히면 아래로 이동해야 하니 dx=0, dy=1, ...
    
    x, y = 0, 0  # 처음 좌표
    direction = 0  # 방향(dx, dy의 방향을 설정하는 용도)
    
    # n^2만큼 반복 (i=1부터 i=n*n까지)
    for i in range(1, (n*n)+1):
        # 빈 리스트에 i 순서대로 넣기
        spiral[y][x] = i
        
        # 이동할 다음 좌표 구하기
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 이동할 좌표가 벽에 부딪히거나(인덱스를 벗어나는 행위) 숫자가 들어있을 시 다음 이동할 좌표 새로 구하기
        if nx >= n or nx < 0 or ny >= n or ny < 0 or spiral[ny][nx] != 0:
            # 방향은 총 4가지(상,하,좌,우)
            direction = (direction + 1) % 4
            
            # 방향 정한 후 다음 이동할 좌표 정하기
            nx = x + dx[direction]
            ny = y + dy[direction]
            
        # x, y에 이동해야 할 다음 좌표 넣기
        x, y = nx, ny
            
    return spiral