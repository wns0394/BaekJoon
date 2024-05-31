import sys

from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(n)]
    key = set(input().rstrip())
    document = set()
    # start = deque()
    start = []
    visited = [[0] * m for _ in range(n)]

    result = 0

    for i in range(n):
        if arr[i][0] != '*':
            start.append((i, 0))
            visited[i][0] = 1
            if arr[i][0].islower():
                key.add(arr[i][0])
            if arr[i][0] == '$' and (i, 0) not in document:
                document.add((i, 0))
                result += 1
        if arr[i][m - 1] != '*':
            start.append((i, m - 1))
            visited[i][m - 1] = 1
            if arr[i][m - 1].islower():
                key.add(arr[i][m - 1])
            if arr[i][m - 1] == '$' and (i, m - 1) not in document:
                result += 1
                document.add((i, m - 1))

    for i in range(m):
        if arr[0][i] != '*':
            start.append((0, i))
            visited[0][i] = 1
            if arr[0][i].islower():
                key.add(arr[0][i])

            if arr[0][i] == '$' and (0, i) not in document:
                result += 1
                document.add((0, i))

        if arr[n - 1][i] != '*':
            start.append((n - 1, i))
            visited[n - 1][i] = 1
            if arr[n - 1][i].islower():
                key.add(arr[n - 1][i])
            if arr[n - 1][i] == '$' and (n - 1, i) not in document:
                result += 1
                document.add((n - 1, i))

    q = deque(start)

    dict = {}
    for i in range(97, 123):
        # dict[i] = []
        dict[chr(i)] = []

    while q:
        x, y = q.popleft()

        if arr[x][y].isupper():
            if arr[x][y].lower() not in key:
                # dict[ord(arr[x][y].lower())].append((x, y))
                dict[arr[x][y].lower()].append((x, y))
                continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '*':
                    continue
                elif arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif arr[nx][ny] == "$" and (nx, ny) not in document and visited[nx][ny] == 0:
                    result += 1
                    document.add((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = 1

                elif arr[nx][ny].islower() and visited[nx][ny] == 0:
                    if arr[nx][ny] not in key:
                        key.add(arr[nx][ny])
                        visited = [[0] * m for _ in range(n)]
                        q.extend(dict[arr[nx][ny]])
                        # q.extend(dict[ord(arr[nx][ny])])
                        # dict[ord(arr[nx][ny])] = []
                        dict[arr[nx][ny]] = []
                    visited[nx][ny] = 1
                    q.append((nx, ny))

                elif arr[nx][ny].isupper() and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    print(result)
