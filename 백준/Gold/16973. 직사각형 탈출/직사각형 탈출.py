from collections import deque


def check(x, y):
    flag = True
    for a, b in wall:
        if x <= a < x + h and y <= b < y + w:
            flag = False
    return flag


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

wall = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            wall.append((i, j))
h, w, sx, sy, fx, fy = map(int, input().split())

visited = [[0] * m for _ in range(n)]

q = deque()

q.append((sx - 1, sy - 1))
visited[sx - 1][sy - 1] = 1
flag = 0

while q:
    x, y = q.popleft()
    if x == fx - 1 and y == fy - 1:
        print(visited[x][y] - 1)
        flag = 1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and 0 <= nx + h - 1 < n and 0 <= ny + w - 1 < m:
            if visited[nx][ny] == 0:
                if check(nx, ny):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
if flag == 0:
    print(-1)
