from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global group

    q = deque()
    q.append((x, y))
    visited[x][y] = group

    while q:
        x, y = q.popleft()

        if arr[x][y] == 'S':
            if visited[x + 1][y] == 0:
                q.append((x + 1, y))
                visited[x + 1][y] = group
            elif visited[x + 1][y] < group:
                return 0

        elif arr[x][y] == 'E':
            if visited[x][y + 1] == 0:
                q.append((x, y + 1))
                visited[x][y + 1] = group
            elif visited[x][y + 1] < group:
                return 0

        elif arr[x][y] == 'N':
            if visited[x - 1][y] == 0:
                q.append((x - 1, y))
                visited[x - 1][y] = group
            elif visited[x - 1][y] < group:
                return 0

        elif arr[x][y] == 'W':
            if visited[x][y - 1] == 0:
                q.append((x, y - 1))
                visited[x][y - 1] = group
            elif visited[x][y - 1] < group:
                return 0
    return 1


n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

count = 0
group = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            group += 1
            count += bfs(i, j)

print(count)
