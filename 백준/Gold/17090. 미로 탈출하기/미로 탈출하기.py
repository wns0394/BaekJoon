import sys

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    global count

    visited[x][y] = 1

    q = deque()
    q.append((x, y))
    flag = False
    now = []
    now.append((x,y))
    while q:
        x, y = q.popleft()

        if arr[x][y] == 'D':
            nx = x + 1
            ny = y
        elif arr[x][y] == 'U':
            nx = x - 1
            ny = y
        elif arr[x][y] == 'L':
            nx = x
            ny = y - 1
        elif arr[x][y] == 'R':
            nx = x
            ny = y + 1

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            q.append((nx, ny))
            visited[nx][ny] = 1
            now.append((nx, ny))
        elif nx < 0 or nx >= n or ny < 0 or ny >= m:
            count += 1
            flag = True
            break
        elif (nx, ny) in check:
            count += 1
            flag = True
            break
    if not flag:
        for a, b in now:
            visited[a][b] = 0
            roop.add((a,b))
    else:
        for a,b in now:
            check.add((a,b))


n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

count = 0

check = set()
roop = set()
for i in range(n):
    for j in range(m):
        if (i,j) in roop:
            continue
        if (i,j) in check:
            count += 1
        else:
            bfs(i, j)

print(count)

