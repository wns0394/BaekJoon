n = int(input())

arr = [[0, 0]]

for _ in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])
    
d = [0] * (n + 1)

for i in range(1, n+1):
    # i날의 최대는 그 전날이랑 같거나 클테니
    d[i] = max(d[i - 1], d[i])
    # i날에 일 시작한다고 생각하면
    # (i + arr[i][0] - 1) 일날 끝난다.
    # 그러므로 i + arr[i][0] - 1 <= n+1을 만족하면
    if i + arr[i][0] - 1 <= n:
        # 끝나는 날짜의 최대값은
        # 끝나는 날짜의 최대 와 i-1일에서최대값 + i일만큼 일하는 금액
        d[i + arr[i][0] - 1] = max(d[i + arr[i][0] - 1], d[i-1] + arr[i][1])

print(d[-1])