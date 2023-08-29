from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dxdown = [0, 1, 0, -1]
dydown = [1, 0, -1, 0]


def dust(x, y):
    here = arr[x][y]
    remain = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != -1:
                newarr[nx][ny] += here // 5
                remain += 1
    newarr[x][y] -= (here // 5) * remain


def airup(x, y, d):
    q = deque()
    q.append((x, y, d))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 0

    while q:
        x, y, d = q.popleft()
        if x == air[0] and y == 0:
            visited[x][y] = 0
            return visited
            break
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                q.append((nx, ny, d))
                visited[nx][ny] = newarr[x][y]
        else:
            d = (d + 1) % 4
            q.append((x, y, d))


def airdown(x,y,d):
    q = deque()
    q.append((x, y, d))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 0

    while q:
        x, y, d = q.popleft()
        if x == air[1] and y == 0:
            visited[x][y] = 0
            return visited
            break
        nx = x + dxdown[d]
        ny = y + dydown[d]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0:
                q.append((nx, ny, d))
                visited[nx][ny] = newarr[x][y]
        else:
            d = (d + 1) % 4
            q.append((x, y, d))

n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

time = 0
air = []
while time < t:
    # 모든 미세먼지에 대해서 확산
    newarr = [a[:] for a in arr]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1 and arr[i][j] != 0:
                dust(i, j)
            if arr[i][j] == -1:
                air.append(i)
    # print(newarr)
    v1 = airup(air[0], 1, 0)
    v2 = airdown(air[1],1,0)
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == air[0]) and arr[i][j] != -1:
                newarr[i][j] = v1[i][j]
            elif 0 < i < air[0] and arr[i][j] != -1:
                newarr[i][0] = v1[i][0]
                newarr[i][m-1] = v1[i][m-1]
            elif (i == air[1] or i == n-1) and arr[i][j] != -1:
                newarr[i][j] = v2[i][j]
            elif air[1] < i < n-1 and arr[i][j] != -1:
                newarr[i][0] = v2[i][0]
                newarr[i][m-1] = v2[i][m-1]
    arr = newarr
    time += 1
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != -1:
            result += arr[i][j]
print(result)