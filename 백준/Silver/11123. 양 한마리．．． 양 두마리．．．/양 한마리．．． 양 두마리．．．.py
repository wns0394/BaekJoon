from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == '#' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#' and visited[i][j] == 0:
                bfs(i, j)
                count += 1
    print(count)