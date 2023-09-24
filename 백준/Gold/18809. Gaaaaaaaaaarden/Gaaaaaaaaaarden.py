
from collections import deque
from itertools import combinations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(new, all, green):
    q = deque()
    cnt = 0
    maxcount = 0
    for x, y in all:
        if (x, y) in green:
            q.append((x, y, 1, 0))
            new[x][y] = 3
            visitedgreen[x][y][0] = 1
        else:
            q.append((x, y, -1, 0))
            new[x][y] = 4
            visitedred[x][y][0] = 1

    while q:

        x, y, color, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 색상이 3(그린) 이라면
                if color == 1 and (new[nx][ny] == 2 or new[nx][ny] == 1) and visitedgreen[nx][ny][0] == 0 and visitedred[nx][ny][0] == 0:
                    q.append((nx, ny, color, count + 1))
                    visitedgreen[nx][ny][0] = 1
                    visitedgreen[nx][ny][1] = count + 1
                if color == 1 and (new[nx][ny] == 2 or new[nx][ny] == 1) and visitedgreen[nx][ny][0] == 0 and visitedred[nx][ny][0] == 1 and visitedred[nx][ny][1] == count + 1:
                    if (nx, ny, -color, count + 1) in q:
                        q.remove((nx, ny, -color, count + 1))
                        maxcount += 1
                if color == -1 and (new[nx][ny] == 2 or new[nx][ny] == 1) and visitedred[nx][ny][0] == 0 and visitedgreen[nx][ny][0] == 0:
                    visitedred[nx][ny][0] = 1
                    visitedred[nx][ny][1] = count + 1
                    q.append((nx, ny, color, count + 1))
                if color == -1 and (new[nx][ny] == 2 or new[nx][ny] == 1) and visitedred[nx][ny][0] == 0 and visitedgreen[nx][ny][0] == 1 and visitedgreen[nx][ny][1] == count + 1:
                    if (nx, ny, -color, count + 1) in q:
                        q.remove((nx, ny, -color, count + 1))
                        maxcount +=1

    return maxcount

n, m, g, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

possible = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            possible.append((i, j))

allp = list(combinations(possible, g + r))

result = 0
for all in allp:
    # all은 가능한 배양액 땅(초록과 빨강 더한거)
    # arr 복사
    new = [a[:] for a in arr]
    # green은 모두 가능한거에서 녹색 개수 조합
    for green in list(combinations(all, g)):
        visitedgreen = [[[0, 0] for _ in range(m)] for _ in range(n)]
        visitedred = [[[0, 0] for _ in range(m)] for _ in range(n)]

        # bfs(new, all, green)
        result = max(result, bfs(new, all, green))

print(result)