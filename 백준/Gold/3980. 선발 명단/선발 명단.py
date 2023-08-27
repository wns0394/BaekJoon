def dfs(player, score):
    global result
    # 11번 선수 -> 모두 포지션 배정 완료
    if player == 11:
        # 더 높은 점수로 선택
        result = max(result, score)
        return
    # 각각의 포지션에 대하여
    for i in range(11):
        # player의 포지션 점수가 0점이 아니고 포지션이 비어있다면
        if arr[player][i] != 0 and visited[i] == 0:
            # 방문처리해주고
            visited[i] = 1
            # 다음 플레이어 탐색해주고 점수에 player의 해당포지션 점수 추가해주기
            dfs(player + 1, score + arr[player][i])
            # 방문 초기화
            visited[i] = 0


t = int(input())

for _ in range(t):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    result = 0
    dfs(0, 0)
    print(result)
