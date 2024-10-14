import sys

from pprint import pprint
import heapq

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# (0,0)에서 시작해서 (n,m)으로 가야한다.
# 벽을 최소 몇 개 부수어야 하냐
# 시작점 정해져있음
# 최단거리 물어봄
# 다익스트라 생각해봐야겠지?

inf = int(1e9)

m, n = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

distance = [[inf] * m for _ in range(n)]

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    distance[0][0] = 0

    while q:
        dist, now_x, now_y = heapq.heappop(q)

        if distance[now_x][now_y] < dist:
            continue

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                cost = dist + int(arr[nx][ny])
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx,ny))


dijkstra(0, 0)

print(distance[n-1][m-1])