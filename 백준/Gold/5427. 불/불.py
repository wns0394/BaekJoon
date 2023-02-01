from collections import deque

t = int(input())

for _ in range(t):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n, m = map(int, input().split())
    result = 'IMPOSSIBLE'
    arr = [list(map(str, input())) for _ in range(m)]

    # #: 벽
    # .: 지나갈 수 있는 공간
    # J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
    # F: 불이 난 공간

    visited_j = [[0] * n for _ in range(m)]
    visited_f = [[0] * n for _ in range(m)]
    # 탈출조건은 각 사이드
    q = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                q.append((0, i, j, 'f'))
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '@':
                q.append((0, i, j, 'j'))
    # print(q)
    queue = deque(q)
    result = 'IMPOSSIBLE'
    while queue:
        time, x, y, a = queue.popleft()
        if a == 'f':
            visited_f[x][y] = 1
        elif a == 'j':
            visited_j[x][y] = 1

        if a == 'j':
            if x == 0 or x == m-1 or y == 0 or y == n-1:
                result = time + 1
                break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if a == 'f':
                    if arr[nx][ny] == '.' or arr[nx][ny] == '@':
                        if visited_f[nx][ny] == 0:
                            queue.append((time, nx, ny, 'f'))
                            visited_f[nx][ny] = 1
                elif a == 'j':
                    if arr[nx][ny] == '.' and visited_f[nx][ny] == 0 and visited_j[nx][ny] == 0:
                        queue.append((time + 1, nx, ny, 'j'))
                        visited_j[nx][ny] = 1
    print(result)