from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    count = 0
    flag = 0
    while q:
        x,y = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                if arr[nx][ny] == 2:
                    flag = 1
    return count, flag

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

li = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            li.append((i,j))
result = 0

comb = list(combinations(li,3))

for i in comb:
    arr[i[0][0]][i[0][1]] = 1
    arr[i[1][0]][i[1][1]] = 1
    arr[i[2][0]][i[2][1]] = 1

    visited = [[0] * m for _ in range(n)]

    safe = 0

    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0 and visited[a][b] == 0:
                count, flag = bfs(a, b)
                if flag != 1:
                    safe += count
    result = max(result, safe)

    arr[i[0][0]][i[0][1]] = 0
    arr[i[1][0]][i[1][1]] = 0
    arr[i[2][0]][i[2][1]] = 0
print(result)