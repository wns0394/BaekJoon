
from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 2 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                if arr[nx][ny] == 0:
                    group.append((nx, ny))


def newbfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    twocount = 0
    flag = 0
    while q:
        x, y = q.popleft()
        twocount += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 2 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                if arr[nx][ny] == 0:
                    flag = 1
    return twocount, flag


n, m = map(int, input().split())

# 0: 빈칸, 1: 내 돌, 2: 상대 돌
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
visited = [[0] * m for _ in range(n)]
count = 0
possible = []
for i in range(n):
    for j in range(m):
        group = []
        if arr[i][j] == 2 and visited[i][j] == 0:
            count += 1
            bfs(i, j)
            if len(set(group)) <= 2:
                possible += group
possible = list(set(possible))
# print(possible)
if len(possible) == 1:
    arr[possible[0][0]][possible[0][1]] = 1
    aa = 0
    visited = [[0] * m for _ in range(n)]
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 2 and visited[a][b] == 0:
                twocount, flag = newbfs(a, b)
                if flag != 1:
                    aa += twocount
    result = max(result, aa)
else:
    allpossible = list(combinations(possible, 2))
    # print(allpossible)
    for i in allpossible:

        # 가능한 위치를 내 돌로 변환
        arr[i[0][0]][i[0][1]] = 1
        arr[i[1][0]][i[1][1]] = 1

        aa = 0
        visited = [[0] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if arr[a][b] == 2 and visited[a][b] == 0:
                    twocount, flag = newbfs(a, b)
                    if flag != 1:
                        aa += twocount
                    # print(ab,i,a,b)
                    # aa += ab
        result = max(result, aa)
        arr[i[0][0]][i[0][1]] = 0
        arr[i[1][0]][i[1][1]] = 0
print(result)
