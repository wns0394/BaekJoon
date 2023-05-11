
from collections import deque

def bfs():
    q = deque()
    q.append((home[0],home[1]))

    while q:
        x,y = q.popleft()

        # 편의점과 락페가 1000이하면 가능하다
        if abs(x-rock[0]) + abs(y-rock[1]) <= 1000:
            return 'happy'
        # 집과 편의점 확인
        for i in range(n):
            # 방문한적 없으면
            if visited[i] == 0:
                # 다음 편의점
                nx,ny = store[i]
                # 이동가능하면
                if abs(x-nx) + abs(y-ny) <= 1000:
                    # 방문처리 후 큐에 담는다
                    visited[i] = 1
                    q.append((nx,ny))
    return 'sad'
t = int(input())
for _ in range(t):
    # 맥주파는 편의점 수
    n = int(input())
    home = [int(i) for i in input().split()]
    store = []
    for i in range(n):
        x, y = map(int,input().split())
        store.append([x,y])
    rock = [int(i) for i in input().split()]

    visited = [0] * (n+1)
    print(bfs())