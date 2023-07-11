import heapq

# 주어진 시작점에서 다른 모든 정점으로의 최단 경로
# => 플로이드 워셜이 아니라 다익스트라다 ㅠㅠ


inf = int(1e9)

# v,e가 많이 크므로 heapq 사용하자
v,e = map(int,input().split())

k = int(input())

arr = [[] for _ in range (v+1)]
# 최단 거리가 들어갈 예정
distance = [inf] * (v+1)

for _ in range(e):
    # a에서 b로가는 가중치 w
    a,b,c = map(int,input().split())
    arr[a].append((b, c))


def dijkstra(start):

    q = []
    heapq.heappush(q,(0,start))
    # 시작값 0
    distance[start] = 0

    while q:
        # 탐색할노드, 거리
        dist, now = heapq.heappop(q)

        # 이미 처리된거라면
        # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클경우 무시한다
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드 확인
        for i in arr[now]:
            # 시작에서 노드거리 + 노드에서 노드의 인접노드 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# k에서 시작하므로
dijkstra(k)

for i in range(1,v+1):
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])