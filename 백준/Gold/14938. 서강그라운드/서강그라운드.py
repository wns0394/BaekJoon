# 모든 지점에서 봐야할듯? -> 플로이드 워셜
inf = int(1e9)

# 지역의 개수 n 수색범위 m 길의 개수 r
n, m, r = map(int, input().split())

item = list(map(int,input().split()))

arr = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            arr[i][j] = 0

for _ in range(r):
    a,b,c = map(int,input().split())
    arr[a][b] = c
    # 양방향이다 둘 다 추가하자
    arr[b][a] = c
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])


# 시작
result_list = []
for i in range(1,n+1):
    # 도착노드
    result = 0
    for j in range(1,n+1):
        if arr[i][j] <= m:
            result += item[j-1]
    result_list.append(result)
print(max(result_list))