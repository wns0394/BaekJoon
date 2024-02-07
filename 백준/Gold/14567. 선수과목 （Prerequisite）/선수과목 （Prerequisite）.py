import sys

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]

indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # 정점 a에서 b로 이동가능
    arr[a].append(b)
    # b로 이동가능하므로
    # 진입차수 1 증가
    indegree[b] += 1

q = deque()

# 진입차수가 0인 노드를 q에 담아주기
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

# 최소 몇 학기에 이수할 수 있는지 담을 result
# 모두 최소 1학기이므로 1로 지정
result = [1] * (n + 1)

while q:
    # 현재 노드
    now = q.popleft()

    for next in arr[now]:
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        indegree[next] -= 1

        # 진입차수가 0이되면 q에 담아주기
        if indegree[next] == 0:
            q.append(next)
            # 학기 + 1
            result[next] = result[now] + 1

print(*result[1:])