from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def broke(h,left):
    x = n - h
    y = 0
    flag = 0

    if left == 1:
        for i in range(m):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                y = i
                flag = 1
                break
    elif left == - 1:
        for i in range(m-1,-1,-1):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                y = i
                flag = 1
                break
    return x,y,flag

def bfs(x,y):
    global cluster
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cluster.append((x,y))
    while q:
        x,y = q.popleft()

        if x == n-1:
            cluster = []
            return cluster

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'x' and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    cluster.append((nx,ny))
    return cluster

def drop(cluster):
    cluster.sort(key=lambda x: (x[1], -x[0]))
    # print(cluster)
    droplist = []

    for x,y in cluster:
        if arr[x+1][y] != 'x':
            droplist.append((x,y))
    mindrop = 101
    for x,y in droplist:
        count = 0

        while True:
            x += 1
            if x >= n:
                break
            if arr[x][y] == 'x' and (x,y) not in cluster:
                break
            count += 1
        mindrop = min(mindrop,count)


    for x,y in cluster:
        arr[x][y] = '.'
        arr[x+mindrop][y] = 'x'
n,m = map(int,input().split())

arr = [list(input()) for _ in range(n)]

cnt = int(input())
stick = list(map(int,input().split()))

left = 1

for h in stick:

    x,y,flag = broke(h,left)
    left *= -1

    # flag가 0이라면 부수지 못했다.
    # 아래 동작 할 필요가 없다.
    if flag == 0:
        continue

    cluster = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        visited = [[0]*m for _ in range(n)]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 'x' and visited[nx][ny] == 0:
                bfs(nx,ny)
                if cluster:
                    drop(cluster)


for i in range(n):
    for j in range(m):
        print(arr[i][j],end='')
    if i != n-1:
        print()