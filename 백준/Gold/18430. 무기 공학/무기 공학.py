import sys

input = sys.stdin.readline

# ┌ ┐ └ ┘ 모양
dx = [(0, 1), (0, 1), (0, -1), (0, -1)]
dy = [(1, 0), (-1, 0), (1, 0), (-1, 0)]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

result = 0


def dfs(x, y, count):
    global result
    # print(x,y,count,visited[x][y])
    result = max(result, count)

    if x == n:
        return

    if visited[x][y] == 0:
        for i in range(4):
            x1, y1 = x + dx[i][0], y + dx[i][1]
            x2, y2 = x + dy[i][0], y + dy[i][1]

            if 0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m:
                if visited[x1][y1] == 0 and visited[x2][y2] == 0:
                    visited[x1][y1] = 1
                    visited[x2][y2] = 1
                    visited[x][y] = 1

                    if y == m - 1:
                        dfs(x + 1, 0, count + arr[x][y] * 2 + arr[x1][y1] + arr[x2][y2])
                    else:
                        dfs(x, y + 1, count + arr[x][y] * 2 + arr[x1][y1] + arr[x2][y2])

                    visited[x1][y1] = 0
                    visited[x2][y2] = 0
                    visited[x][y] = 0
    if y == m - 1:
        dfs(x + 1, 0, count)
    else:
        dfs(x, y + 1, count)


dfs(0, 0, 0)

print(result)