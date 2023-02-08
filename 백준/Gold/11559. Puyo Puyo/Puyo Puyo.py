

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[0] * 6 for _ in range(12)]
    visited[x][y]= 1
    # 4번 들어갔는지 count
    count = []
    count.append((x,y))
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6:
                if arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    count.append((nx, ny))
    # print(count)
    # count의 길이가 4이상이면 터트린다.
    if len(count) >= 4:
        for x,y in count:
            arr[x][y] = '.'
        return True
    return False

arr =[list(map(str,input())) for _ in range(12)]
# visited = [[0] * 6 for _ in range(12)]
cnt = 0
result = True
while result:
    result = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
            # if arr[i][j] != '.' and visited[i][j] == 0:
                result |= bfs(i, j)

    if result:
        cnt += 1
        for j in range(6):
            for i in range(10,-1,-1):
                for k in range(11,i,-1):
                    if arr[i][j] != '.' and arr[k][j] == '.':
                        arr[i][j], arr[k][j] = arr[k][j], arr[i][j]
                        break
print(cnt)
