from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y,cnt))
    visited[x][y] = 1
    new[x][y] = cnt
    while q:
        x,y,cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx,ny,cnt))
                    visited[nx][ny] = 1
                    new[nx][ny] = cnt

def new_bfs(x,y,a):
    global result
    q = deque()
    q.append((x,y,a))
    visited = [[0]* n for _ in range(n)]
    visited[x][y] = 1

    while q:
        x,y,a = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if new[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx,ny,a))
                    visited[nx][ny] = visited[x][y] + 1
                if new[nx][ny] > a:
                    result = min(result,visited[x][y])

                    return result
n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
new = [[0]* n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j,cnt)
            cnt += 1

new_visited = [[0]* n for _ in range(n)]
result = 1000
for i in range(n):
    for j in range(n):
        for a in range(1,cnt):
            if new[i][j] == a:
                new_bfs(i,j,a)
print(result-1)