from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def right(x,y):
    global new
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((x, y, 5))

    while q:
        x, y, t = q.popleft()

        if not visited[x][y]:
            new[x][y] += t
        visited[x][y] = 1

        if t < 1:
            break

        # 오른쪽 위
        if 0 <= x - 1 < n and 0 <= y + 1 < m and (x, y) not in up_wall and (x-1, y) not in right_wall and \
                visited[x - 1][y + 1] == 0:
            q.append((x - 1, y + 1, t - 1))
        # 오른쪽 밑
        if 0 <= x + 1 < n and 0 <= y + 1 < m and (x+1, y) not in up_wall and (x+1, y) not in right_wall and \
                visited[x + 1][y + 1] == 0:
            q.append((x + 1, y + 1, t - 1))
        # 그냥 오른쪽
        if 0 <= x < n and 0 <= y+1 < m and (x, y) not in right_wall and visited[x][y+1] == 0:
            q.append((x , y+1, t - 1))

def left(x,y):
    global new
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((x, y, 5))

    while q:
        x, y, t = q.popleft()

        if not visited[x][y]:
            new[x][y] += t
        visited[x][y] = 1

        if t < 1:
            break

        # 왼쪽 위
        if 0 <= x - 1 < n and 0 <= y - 1 < m and (x, y) not in up_wall and (x-1, y-1) not in right_wall and \
                visited[x - 1][y - 1] == 0:
            q.append((x - 1, y - 1, t - 1))
        # 왼쪽 밑
        if 0 <= x + 1 < n and 0 <= y - 1 < m and (x+1, y) not in up_wall and (x+1, y-1) not in right_wall and \
                visited[x + 1][y - 1] == 0:
            q.append((x + 1, y - 1, t - 1))
        # 그냥 왼쪽
        if 0 <= x < n and 0 <= y-1 < m and (x, y-1) not in right_wall and visited[x][y-1] == 0:
            q.append((x , y-1, t - 1))

def up(x, y):
    global new
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((x, y, 5))

    while q:
        x, y, t = q.popleft()

        if not visited[x][y]:
            new[x][y] += t
        visited[x][y] = 1

        if t < 1:
            break

        # 오른쪽 위
        if 0 <= x - 1 < n and 0 <= y + 1 < m and (x, y) not in right_wall and (x, y + 1) not in up_wall and \
                visited[x - 1][y + 1] == 0:
            q.append((x - 1, y + 1, t - 1))
        # 왼쪽 위
        if 0 <= x - 1 < n and 0 <= y - 1 < m and (x, y - 1) not in right_wall and (x, y - 1) not in up_wall and \
                visited[x - 1][y - 1] == 0:
            q.append((x - 1, y - 1, t - 1))
        # 그냥 위
        if 0 <= x - 1 < n and 0 <= y < m and (x, y) not in up_wall and visited[x - 1][y] == 0:
            q.append((x - 1, y, t - 1))


def down(x, y):
    global new
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((x, y, 5))

    while q:
        x, y, t = q.popleft()

        if not visited[x][y]:
            new[x][y] += t
        visited[x][y] = 1

        if t < 1:
            break

        # 오른쪽 아래
        if 0 <= x + 1 < n and 0 <= y + 1 < m and (x, y) not in right_wall and (x + 1, y + 1) not in up_wall and \
                visited[x + 1][y + 1] == 0:
            q.append((x + 1, y + 1, t - 1))
        # 왼쪽 아래
        if 0 <= x + 1 < n and 0 <= y - 1 < m and (x, y - 1) not in right_wall and (x + 1, y - 1) not in up_wall and \
                visited[x + 1][y - 1] == 0:
            q.append((x + 1, y - 1, t - 1))
        # 그냥 아래
        if 0 <= x + 1 < n and 0 <= y < m and (x + 1, y) not in up_wall and visited[x + 1][y] == 0:
            q.append((x + 1, y, t - 1))


def move():
    newarr = [a[:] for a in new]
    for i in range(n):
        for j in range(m):
            if new[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and new[i][j] > new[nx][ny]:
                        if (d == 0 and (i, j) not in right_wall) or (d == 1 and (i, j - 1) not in right_wall) or (
                                d == 2 and (i, j) not in up_wall) or (d == 3 and (i + 1, j) not in up_wall):
                            newarr[nx][ny] += (new[i][j] - new[nx][ny]) // 4
                            newarr[i][j] -= (new[i][j] - new[nx][ny]) // 4

    return newarr

def side():
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                if new[i][j] >0:
                    new[i][j] -= 1

def checkpoint():
    for x,y in check:
        if new[x][y] < k:
            return False
    return True
# n*m 배열
# k -> 조사해야하는 온도
n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
new = [[0] * m for _ in range(n)]
li = []

check = []
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 5:
            li.append((i, j, arr[i][j]))

        if arr[i][j] == 5:
            check.append((i, j))
w = int(input())

right_wall = []
up_wall = []
for _ in range(w):
    # t == 0 -> (x,y) 와 (x-1,y) 사이에 벽
    # 즉 내 위에 벽
    # t == 1 -> (x,y) 와 (x,y+1) 사이에 벽
    # 즉 내 오른쪽 벽
    x, y, t = map(int, input().split())

    if t == 0:
        up_wall.append((x - 1, y - 1))
    elif t == 1:
        right_wall.append((x - 1, y - 1))

result = 0
flag = 1
while True:
    result += 1

    for x,y,d in li:
        if d == 1:
            right(x,y+1)
        elif d == 2:
            left(x,y-1)
        if d == 3:
            up(x - 1, y)
        elif d == 4:
            down(x + 1, y)
            

    newarr = move()

    new = newarr

    side()

    if checkpoint():
        break

    if result > 100:
        result = 101
        break


print(result)