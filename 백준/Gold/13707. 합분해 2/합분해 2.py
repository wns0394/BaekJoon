n, k = map(int,input().split())

# d[i][j] -> j개 사용해서 i를 만드는 경우의 수
d = [[0]*(5001) for _ in range(5001)]

# 0개 사용해서 0을 만드는 방법은 무조건 1개 이므로
d[0][0] = 1

for i in range(n+1):
    for j in range(1,k+1):
        d[i][j] = (d[i][j-1] + d[i-1][j]) % 1000000000
print(d[n][k])