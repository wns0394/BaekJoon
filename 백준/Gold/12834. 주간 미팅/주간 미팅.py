import sys

input = sys.stdin.readline

import heapq

# 팀원의수 n, 장소의 수 v, 도로의 수 e
n, v, e = map(int, input().split())

# kist의 위치 a, cr위치 b
a, b = map(int, input().split())

# 팀원 n명의 집의 위치 h_i
house = list(map(int, input().split()))

inf = int(1e9)

arr = [[] for i in range(v + 1)]

distance_a = [inf] * (v + 1)
distance_b = [inf] * (v + 1)

for _ in range(e):
    # 도로의 양 끝 장소 x,y 길이 l
    x, y, l = map(int, input().split())
    arr[x].append((y, l))
    arr[y].append((x, l))


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(a, distance_a)
dijkstra(b, distance_b)

# for i in range(1, v + 1):
#     if distance_a[i] == inf:
#         distance_a[i] = -1
#     if distance_b[i] == inf:
#         distance_b[i] = -1

result = 0
for i in house:
    if distance_a[i] == inf:
        distance_a[i] = -1
    if distance_b[i] == inf:
        distance_b[i] = -1

    result += distance_a[i] + distance_b[i]

print(result)
