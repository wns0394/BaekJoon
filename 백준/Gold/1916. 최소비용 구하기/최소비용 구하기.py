import heapq

# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라.
# -> 출발지 정해져있다. 다익스트라
n = int(input())
m = int(input())

inf = int(1e10)
arr = [[] for _ in range(n + 1)]
distance = [inf] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

s,e = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            # 이미 처리됨
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)
print(distance[e])