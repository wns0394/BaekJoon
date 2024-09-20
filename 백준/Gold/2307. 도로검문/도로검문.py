import sys

from pprint import pprint
import heapq

input = sys.stdin.readline


def dijkstra(s, a, b):
    q = []

    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            if now == a and i[0] == b:
                continue
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = now
                heapq.heappush(q, (cost, i[0]))


def find(e):
    if e == 1:
        shortes.append(e)
        return
    find(path[e])
    shortes.append(e)


n, m = map(int, input().split())

inf = int(1e9)

# 도로는 모두 양방향
# 출발은 항상 1번 탈출은 항상 n번
# 출발지가 정해져 있으므로 다익스트라 사용

arr = [[] for i in range(n + 1)]

distance = [inf] * (n + 1)

path = [0] * (n + 1)
path[1] = 1
for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))
    arr[b].append((a, t))

dijkstra(1, 0, 0)

first = distance[n]


shortes = []
find(n)

result = 0
for i in range(len(shortes) - 1):
    distance = [inf] * (n + 1)
    arr[shortes[i]]

    dijkstra(1, shortes[i], shortes[i + 1])

    if result < distance[n]:
        result = distance[n]

if result == inf:
    print(-1)
else:
    print(result-first)
