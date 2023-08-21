import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, z):
    global count
    arr[x][y] = 'T'
    if x == 0 and y == m - 1 and z == k:
        # if (0,2) in path:
        #     print(path)
        count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == '.':
                arr[nx][ny] = 'T'
                # path.append((nx,ny))
                dfs(nx, ny, z + 1)
                arr[nx][ny] = '.'
                # path.pop()


n, m, k = map(int, input().split())
arr = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

count = 0
# path = []
# path.append((n-1,0))

dfs(n - 1, 0, 1)
print(count)
