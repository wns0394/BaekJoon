import sys
from collections import deque

n, k = map(int, input().split())

visited = [0] * (100001)

q = deque()
q.append(n)
visited[n] = 0
parent = [0] * (100001)
while q:
    x = q.popleft()

    # 수빈의 위치보다 동생의 위치가 작으면 계속 빼줘야한다.
    if n >= k:
        print(n - k)
        for i in range(n,k-1,-1):
            print(i, end=' ')
        break
    if x == k:
        print(visited[k])
        result = []
        result.append(k)
        for i in range(visited[k]):
            result.append(parent[result[-1]])
        print(*result[::-1], sep=' ')
        break
    for next in (x - 1, x + 1, x * 2):
        if 0 <= next < 100001 and visited[next] == 0:
            if next == x*2 and next != 0:
                q.appendleft(next)
                parent[next] = x
                visited[next] = visited[x] + 1
            else:
                q.append(next)
                parent[next] = x
                visited[next] = visited[x] + 1
