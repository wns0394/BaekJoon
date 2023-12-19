
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global flag
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == arr[x][y]:
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                dfs(nx, ny)
                visited[nx][ny] = 0
            elif visited[nx][ny] == 1 and visited[x][y] >= 3:
                flag = True
                # print(flag)
                return flag
    return flag


n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
flag = False
result = 'No'
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j)
        if flag:
            result = 'Yes'
            break
print(result)