inf = int(1e9)

# v 마을 수, e 도로 수
v, e = map(int, input().split())

arr = [[inf] * (v + 1) for _ in range(v + 1)]

# 자기 자신을 0으로 두면 안된다. 돌아오므로
# for i in range(1, v + 1):
#     for j in range(1, v + 1):
#         if i == j:
#             arr[i][j] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for i in range(1,v+1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            arr[a][b] = min(arr[a][b], arr[a][i]+arr[i][b])

# 다시 시작점으로 돌아와야 하므로
result = int(1e9)
for i in range(1,v+1):
    result = min(result,arr[i][i])

if result == int(1e9):
    print(-1)
else:
    print(result)