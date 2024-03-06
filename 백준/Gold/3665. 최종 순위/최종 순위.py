import sys

input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    indegree = [0] * (n + 1)
    graph = [[] * (n + 1) for _ in range(n + 1)]
    # 1등 부터 팀 나열되어있음
    team = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            # i번째 팀은 그 밑에 팀들로 이동 가능
            graph[team[i]].append(team[j])
            # j번째 팀들은 i에서부터 오는거이므로 진입차수 증가
            indegree[team[j]] += 1

    # print(graph)
    # print(indegree)
    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        # print(a,b)
        # a의 진입차수가 크다 -> a의 등수가 b보다 밑이다.
        # b에서 a로 갔었다 원래
        # a에서 b로 가도록 바꾸자

        # if indegree[a] >= indegree[b] and a in graph[b]:
        #     graph[a].append(b)
        #     graph[b].remove(a)
        #     indegree[a] -= 1
        #     indegree[b] += 1
        #     # print(graph)
        #     # print(indegree)
        # elif indegree[a] <= indegree[b] and b in graph[a]:
        #     graph[b].append(a)
        #     graph[a].remove(b)
        #     indegree[b] -= 1
        #     indegree[a] += 1
        flag = True
        for i in graph[a]:
            if i == b:
                graph[b].append(a)
                graph[a].remove(b)
                indegree[b] -= 1
                indegree[a] += 1
                flag = False

        if flag:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    if not q:
        print('IMPOSSIBLE')
        continue

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    if len(result) != n:
        print('IMPOSSIBLE')
    else:
        print(*result)