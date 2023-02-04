from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽 아니고 안가봤으면
                if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    q.append((nx, ny, w))
                    visited[nx][ny][w] = visited[x][y][w] + 1
                # 벽이고 벽 안부시고 안가봤으면
                if arr[nx][ny] == 1 and w == 0 and visited[nx][ny][w] == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][w] + 1
    return -1

n,m = map(int, input().split())

arr = [list(map(int,input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
print(bfs())