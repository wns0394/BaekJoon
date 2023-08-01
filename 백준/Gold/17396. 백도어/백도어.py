import sys
import heapq

# 첫 번째 줄에 안 들키고 가는데 걸리는 최소 시간을 출력한다.
# 만약 상대 넥서스까지 갈 수 없으면 -1을 출력한다.
# 다익스트라

inf = int(1e10)

# 분기점 n 분기점들을 잇는 길의 수 m
n, m = map(int, input().split())

view = list(map(int, input().split()))
view[-1] = 0
arr = [[] for i in range(n + 1)]

distance = [inf] * (100001)
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향
    arr[a].append((b, c))
    arr[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]

            if view[i[0]] != 1 and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(0)
if distance[n - 1] != inf:
    print(distance[n - 1])
else:
    print(-1)
