from collections import deque

dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    vistied[x][y] = 1
    while q:
        x, y = q.popleft()

        if x == n - 1 and y == n - 1:
            return True
        distance = arr[x][y]

        for i in range(2):
            nx = x + dx[i] * distance
            ny = y + dy[i] * distance
            if 0 <= nx < n and 0 <= ny < n and vistied[nx][ny] == 0:
                q.append((nx, ny))
                vistied[nx][ny] = 1
    return False


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
vistied = [[0]* n for _ in range(n)]
if bfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')
