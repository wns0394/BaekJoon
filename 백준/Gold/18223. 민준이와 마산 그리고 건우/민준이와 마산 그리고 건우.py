import heapq

inf = int(1e9)

v, e, p = map(int, input().split())

arr = [[] for i in range(v + 1)]

distance = [inf] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    # 양방향 이므로 a에서 b까지 거리 c
    # b에서 a까지의 거리 c 둘 다 넣어줌
    arr[a].append((b, c))
    arr[b].append((a, c))

def dijkstra(start):
    q = []
    # 시작점으로가는 거리 0으로 설정
    heapq.heappush(q,(0,start))
    # 시작점까지으 ㅣ거리 0
    distance[start] = 0

    while q:
        # 최단거리 짧은거 뽑아내기
        dist, now = heapq.heappop(q)
        # 이미 처리된거라면 진행
        if distance[now] < dist:
            continue
        # 현재 노드에 연결된 노드들 확인
        for i in arr[now]:
            # 지금 노드를 거쳐서 다른노드를 가는 거리
            cost = dist + i[1]
            # 그게 지금까지의 최소 거리보다 짧으면
            if cost < distance[i[0]]:
                # 최소거리 갱신
                distance[i[0]] = cost
                # 최단거리와 노드 삽입
                heapq.heappush(q, (cost, i[0]))
    return distance

# 1(시작) -> v(마산) 이 1(시작) -> p(건우) -> v(마산) 같다면

if dijkstra(1)[v] == dijkstra(1)[p] + dijkstra(p)[v]:
    print('SAVE HIM')
else:
    print('GOOD BYE')