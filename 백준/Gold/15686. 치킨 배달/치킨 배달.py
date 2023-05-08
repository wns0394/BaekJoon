from itertools import combinations
n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

li = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            li.append([i,j])
        elif arr[i][j] == 1:
            home.append((i,j))

ch = list(combinations(li,m))
r = []
for i in ch:
    d = 0
    for h in home:
        result = []
        for j in i:
            # x y 는 치킨집
            x = j[0]
            y = j[1]
            # result에 들어가는거는 각 집에서 치킨집 까지의 거리
            result.append(abs(h[0]-x) + abs(h[1]-y))
        d += sorted(result)[0]
    r.append(d)
# print(r)
print(sorted(r)[0])