
# 돌의 개수
n = int(input())

arr = [[0, 0]]
for _ in range(n - 1):
    small, big = map(int, input().split())
    arr.append([small, big])

# 큰 점프
k = int(input())

d = [0] * (n + 1)

d[0] = 0
if n == 1:
    print(0)
elif n == 2:
    print(arr[1][0])
else:
    # 1까지의 최소는 1로가는 작은 점프
    d[1] = arr[1][0]
    # 2로가는 최소는
    # 1로가는 최소에서 2로가는 작은점프 d[1]+arr[2][0]
    # 바로 2로가는 큰점프 arr[2][1]
    # 2개 중 최소값
    # d[2] = min(d[1] + arr[2][0], arr[2][1])
    d[2] = min(d[1] + arr[2][0], arr[1][1])

    for i in range(3, n):
        # i로 가는 최소는
        # i-1에서 작은점프로 다음돌로 이동하는 d[i-1] + arr[i][0]
        # i-2에서 큰 점프로 1개의 돌을 건너뛰어 이동하는 d[i-2] + arr[i][1]
        # d[i] = min(d[i - 1] + arr[i][0], d[i - 2] + arr[i][1])
        d[i] = min(d[i - 1] + arr[i][0], d[i - 2] + arr[i-1][1])

    result = d[n-1]

    for i in range(3,n):
        dp = d[:]
        dp[i] = d[i-3] + k
        for j in range(i+1,n):
            # dp[j] = min(dp[j - 1] + arr[j][0], dp[j - 2] + arr[j][1])
            dp[j] = min(dp[j - 1] + arr[j][0], dp[j - 2] + arr[j-1][1])

        if result > dp[n-1]:
            result = dp[n-1]
    print(result)