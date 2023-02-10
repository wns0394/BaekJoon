
from collections import deque

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(z, x, y):
    q = deque()
    q.append((z, x, y))
    visited[z][x][y] = 1

    while q:
        z, x, y = q.popleft()

        if new_arr[z][x][y] == 'E':
            # print(z,x,y)
            return f'Escaped in {visited[z][x][y] - 1} minute(s).'
            break
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if new_arr[nz][nx][ny] == '.' and visited[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                elif new_arr[nz][nx][ny] == 'E' and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    q.append((nz, nx, ny))
    return 'Trapped!'

while True:

    l, r, c = map(int, input().split())
    arr = [[list(map(str, input())) for _ in range(r + 1)] for _ in range(l)]
    new_arr = [[[0] * c for _ in range(r)] for _ in range(l)]
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    if l == 0 and r == 0 and c == 0:
        break
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if arr[k][i][j]:
                    new_arr[k][i][j] = arr[k][i][j]
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if new_arr[k][i][j] == 'S' and visited[k][i][j] == 0:
                    # print(k,i,j)
                    print(bfs(k, i, j))
    # print(visited)