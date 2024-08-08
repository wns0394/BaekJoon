import sys

from heapq import heappop, heappush

input = sys.stdin.readline

# 정점 n개 간선 m개 무방향 그래프
# s에서 e로 연결되는 간선의 가중치의 합이 최소가 되게
# 출발 도착지점 정해져있음 && 가중치의 합이 최소
# -> 다익스트라다

n, m = map(int, input().split())

# 각 노드에 연결되어 있는 정보를 담는 리스트
arr = [[] for _ in range(n + 1)]

inf = int(1e9)

# 출발지로부터 거리를 담을 distance
distance = [inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a노드에서 b로 가는 비용 c
    # b노드에서 a로 가는 비용 c
    arr[a].append((b, c))
    arr[b].append((a, c))

s, e = map(int, input().split())

def dijkstra(start):
    q = []
    # 시작 노드로 가는 최단 경로는 0이다.
    heappush(q,(0,start))

    # 자기자신까지의 거리는 0이다
    distance[start] = 0

    while q:
        # 가장 거리가 짧은 노드에 대한 정보 꺼내기
        # dist 는 거리이고 now는 노드 번호
        dist, now = heappop(q)

        # 이미 처리된 적이 있는 노드라면
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in arr[now]:
            # 비용 확인
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q,(cost,i[0]))

dijkstra(s)

print(distance[e])