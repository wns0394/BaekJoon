from collections import deque

dx = [-1,0,1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

n, m = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

min_result = 1000

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

max_result = 0
while q:
    x,y = q.popleft()

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))
                max_result = max(max_result,arr[nx][ny])

print(max_result-1)