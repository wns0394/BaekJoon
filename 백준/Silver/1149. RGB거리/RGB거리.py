
n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]


d = [[0,0,0] for _ in range(n+1)]
# 처음에 빨간색 선택했을때
d[0][0] = arr[0][0]
# 처음에 초록색 선택했을때
d[0][1] = arr[0][1]
# 처음에 파란색 선택했을때
d[0][2] = arr[0][2]
for i in range(1,n):
    # i번째가 빨간색에는 그 전에 파랑과 초록중에 최소값과 현재 빨간색의 비용을 더한다.
    d[i][0] = min(d[i-1][1],d[i-1][2]) + arr[i][0]
    # i번째가 초록색에는 그 전에 파랑과 빨강중에 최소값과 현재 초록색의 비용을 더한다.
    d[i][1] = min(d[i-1][0],d[i-1][2]) + arr[i][1]
    d[i][2] = min(d[i-1][0],d[i-1][1]) + arr[i][2]
# 가장 적은 비용 출력
print(min(d[n-1][0],d[n-1][1],d[n-1][2]))
