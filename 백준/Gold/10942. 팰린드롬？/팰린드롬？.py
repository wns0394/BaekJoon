import sys

input = sys.stdin.readline

# 1 <= n <= 2000
# 1 <= m <= 100000
# 완탐돌면 시간제한이 0.5초라서 무조건 시간초과가 난다.

n = int(input())

arr = [0] + list(map(int, input().split()))

m = int(input())

# d[i][j] => i부터 j까지가 팰린드롬인지 확인하는
# 만약 d[i+1][j-1]가 1이라면 팰린드롬이다.
# 그렇다면 d[i][j]은
# d[i+1][j-1]가 팰린드롬인지 확인하고 arr[i] arr[j]가 서로 같은지 확인하면 된다

d = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][i] = 1

for i in range(1, n):
    if arr[i] == arr[i + 1]:
        d[i][i + 1] = 1

# j먼저 조사하는 이유는
# 행 먼저 조사하게 되면 d[i+1][j-1]이 비어있게 되어 원하는 해답을 얻을 수 없다
for j in range(1,n+1):
    for i in range(1,n):
        if d[i+1][j-1] == 1 and arr[i] == arr[j]:
            d[i][j] = 1


for _ in range(m):
    s, e = map(int, input().split())
    print(d[s][e])
