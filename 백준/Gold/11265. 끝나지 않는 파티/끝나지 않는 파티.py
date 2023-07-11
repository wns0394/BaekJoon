# 모든 노드의 최단 거리 -> 플로이드 워셜
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b],arr[a][i] + arr[i][b])

for _ in range(m):
    a, b, c = map(int, input().split())
    # 1에서 1로 가는게 0,0인덱스이므로 a-1,b-1
    # c시간내로 올 수 있다면
    if arr[a-1][b-1] <= c:
        print('Enjoy other party')
    else:
        print('Stay here')