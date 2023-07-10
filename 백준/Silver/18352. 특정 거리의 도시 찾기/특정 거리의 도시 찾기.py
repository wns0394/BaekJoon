import heapq
# X로 부터 출발하여 도달 가능한 모든 도시중에서 최단 거리가 K인 모든 도시 번호 출력
# 출발지가 하나이므로 다익스트라 사용
# n,m,k 가 매우 크므로 heapq 사용

inf = int(1e9)
n,m, k, x = map(int,input().split())

arr = [[] for _ in range(n+1)]

distance = [inf] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    # a에서 b로 가는게 1이든다
    arr[a].append((b,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(x)

if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)