from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    visited[x][y] = 1
    group = []
    group.append((x, y))
    while q:
        x, y, z = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if abs(arr[nx][ny] - z) >= l and abs(arr[nx][ny] - z) <= r and visited[nx][ny] == 0:
                    q.append((nx, ny, arr[nx][ny]))
                    visited[nx][ny] = 1
                    group.append((nx, ny))
    return group


n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                # visited[i][j] = 1
                g = bfs(i, j, arr[i][j])
                if len(g) > 1:
                    flag = 1
                    total = 0
                    for x, y in g:
                        total += arr[x][y]
                    for x, y in g:
                        arr[x][y] = int(total / len(g))
    if flag == 0:
        print(result)
        break
    result += 1
