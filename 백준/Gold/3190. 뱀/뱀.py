from collections import deque


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,d):
    global count, move
    q = deque()
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    q.append((x,y,d))
    snake = deque()
    snake.append((x,y))
    while q:
        x,y,d = q.popleft()

        for i in move:
            if count != i[0]:
                continue
            if count == i[0] and i[1] == 'D':
                d = (d+1) % 4
            elif count == i[0] and i[1] == 'L':
                d = (d-1) % 4
        count += 1

        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0 and (nx,ny) not in snake:
                q.append((nx,ny,d))
                snake.append((nx,ny))
                snake.popleft()
            elif arr[nx][ny] == 0 and (nx,ny) in snake:
                return count
            elif arr[nx][ny] == 1:
                q.append((nx,ny,d))
                snake.append((nx,ny))
                arr[nx][ny] = 0

    return count
# 보드의 크기
n = int(input())

# 사과의 개수
k = int(input())

arr = [[0]* n for _ in range(n)]

apple = []
for _ in range(k):
    x,y = map(int,input().split())
    apple.append((x,y))
    arr[x-1][y-1] = 1

# 뱀의 방향 변환 횟수
l = int(input())

move = []
for _ in range(l):
    a = list(input().split())
    move.append((int(a[0]),a[1]))

count = 0
bfs(0,0,0)
print(count)
