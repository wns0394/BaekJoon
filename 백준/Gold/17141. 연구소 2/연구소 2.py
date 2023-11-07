
from collections import deque
from itertools import combinations

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a):

    q = deque()

    visited = [[0]*n for _ in range(n)]

    for i in a:
        q.append(i)
        visited[i[0]][i[1]] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and (arr[i][j] == 0 or arr[i][j] == 2):
                count += 1

    return visited[x][y] - 1,count

n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

virus = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus.append((i,j))

all_virus = list(combinations(virus,m))


result = 10000
for i in all_virus:
    time,count = bfs(i)
    if time < result and count == 0:
        result = time

if result == 10000:
    print(-1)
else:
    print(result)