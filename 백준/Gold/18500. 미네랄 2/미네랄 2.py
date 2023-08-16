import sys
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def broke(height, direction):
    x, y = n-height, 0

    # 왼쪽에서 부터 파괴
    if left % 2 == 0:
        for i in range(m):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                y = i
                break

    # 오른쪽부터 파괴
    elif left % 2 == 1:
        for i in range(m - 1, -1, -1):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                y = i
                break
    return x, y


def bfs(x, y):
    global cluster
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cluster.append((x,y))
    while q:
        x, y = q.popleft()

        # 바닥에 닿으면
        if x == n - 1:
            # 분리된게 아니다.
            cluster = []
            return cluster

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'x' and visited[nx][ny] == 0:
                    cluster.append((nx, ny))
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return cluster

def move(cluster):
    # 높이 최대는 100이므로
    drop = 101
    # cluster에서 전부 확인하니까 자기 밑에 미네랄있는 클러스터가 떨어질 공간 없다고 판단
    # cluster중에서 높이가 제일 낮은애들만 골라서 확인해야할듯
    cluster.sort(key=lambda x: (x[1], -x[0]))
    for a,b in cluster:
        count = 0
        while True:
            a += 1
            if a >= n or (arr[a][b] == 'x' and not visited[a][b]):
                break
            # 1회 늘려준다
            count += 1
        # 바닥에 닿는 최소 높이 갱신
        drop = min(drop,count)
    # 아래로 떨구기
    for a,b in cluster:
        arr[a+drop][b] = 'x'
        arr[a][b] = '.'
    return True
n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

s = int(input())
stick = list(map(int, input().split()))

left = 1

for height in stick:

    left += 1
    # 부수는 함수(높이,왼,오판단)
    # x,y는 부순 애 좌표
    x, y = broke(height, left)
    cluster = []
    # 부순거 근처에 날라댕기는 클러스터 있는지 확인하기 위해
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        visited = [[0] * m for _ in range(n)]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 'x' and visited[nx][ny] == 0:
                bfs(nx, ny)

                if cluster:
                    move(cluster)
                    break
for i in range(n):
    for j in range(m):
        print(arr[i][j],end='')
    print()
