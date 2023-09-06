def dfs(x,y,idx):
    global count
    # 방문처리
    visited[x][y] = idx

    if arr[x][y] == 'U':
        nx = x - 1
        ny = y
        if visited[nx][ny] == 0:
            dfs(nx,ny,idx)
        elif visited[nx][ny] == idx:
            count += 1
            return
        else:
            return
    elif arr[x][y] == 'D':
        nx = x + 1
        ny = y
        if visited[nx][ny] == 0:
            dfs(nx, ny, idx)
        elif visited[nx][ny] == idx:
            count += 1
            return
        else:
            return
    elif arr[x][y] == 'R':
        nx = x
        ny = y + 1
        if visited[nx][ny] == 0:
            dfs(nx, ny, idx)
        elif visited[nx][ny] == idx:
            count += 1
            return
        else:
            return
    elif arr[x][y] == 'L':
        nx = x
        ny = y - 1
        if visited[nx][ny] == 0:
            dfs(nx, ny, idx)
        elif visited[nx][ny] == idx:
            count += 1
            return
        else:
            return
# 구역을 구하는거라면 dfs를 사용해보자
n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

count = 0
idx = 1
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(i,j,idx)
            idx += 1
print(count)