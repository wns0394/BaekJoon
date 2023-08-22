from collections import deque

s = int(input())

q = deque()
# 이모티콘 1개 클립 이모티콘 0개
q.append((1,0))

# visited[i][j] -> i개번째에 j개의 클립 만드는 시간
visited = [[0] * 1001 for _ in range(1001)]

while q:
    i, clip = q.popleft()
    # 목표개수에 도달하면
    if i == s:
        print(visited[i][clip])
        break

    # 현재 이모티콘 복사하기
    if visited[i][i] == 0:
        # clip을 i개로 복사했으니까 1초 더해준다
        visited[i][i] = visited[i][clip] + 1
        # 이모티콘 i개 클립 i개 q에 저장
        q.append((i,i))

    # 다음은 현재 이모티콘에서 클립만큼 더하거나 1개를 뺀다
    for next in (i+clip, i-1):
        # 방문한적없고 구역 내 이면
        if 2 <= next < 1001 and visited[next][clip] == 0:
            visited[next][clip] = visited[i][clip] + 1
            q.append((next,clip))