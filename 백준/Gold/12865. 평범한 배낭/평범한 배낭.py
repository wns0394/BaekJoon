
# 물품의 수 n
# 버틸 수 있는 무게 k
n, k = map(int,input().split())

arr = [[0,0]]

for _ in range(n):
    # w : 물건의 무게
    # v : 가치
    w,v = map(int,input().split())
    arr.append([w,v])

d = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = arr[i][0]
        value = arr[i][1]

        # 가방에 넣을 수 없으면
        if j < weight:
            # 위의 값 그대로 가져오기
            d[i][j] = d[i-1][j]
        # 가방에 넣을 수 있다면
        else:
            d[i][j] = max(d[i-1][j],d[i-1][j-weight] + value)

print(d[n][k])