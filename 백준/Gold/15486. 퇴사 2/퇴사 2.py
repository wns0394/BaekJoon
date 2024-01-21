import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])

d = [0] * (n + 1)

for i in range(1, n + 1):
    # i번째 요일의 최대값은 그전날보다 무조건 크거나 같다.
    d[i] = max(d[i], d[i - 1])

    # i번째 요일에 일을 한다면
    # i + t_i - 1 일에 끝날테니 그게 n일 안에 존재하고
    if i + arr[i-1][0] - 1 <= n:
        # i + arr[i-1][0] - 1 요일의 최대값은
        # 그 당일이 최대이거나 아니라면
        # i-1번째 일의 최대에서 i번째 요일의 받은 금액을 더한 것과 비교
        d[i + arr[i-1][0] - 1] = max(d[i + arr[i-1][0] - 1], d[i-1] + arr[i-1][1])

print(d[-1])