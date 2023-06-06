
n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

# d[k] => k원이 되는 경우의 수
d = [0 for _ in range(k+1)]
d[0] = 1
# 코인 돌면서
for i in coin:
    # 목표 금액들
    for j in range(i,k+1):
        # 목표금액에서 코인을 뺀게 0보다 크다면
        # 아직 더 채워야한다면
        if j-i >= 0:
            # i원 만큼 더하는거니까 (j-i)원에서 더하면 된다
            d[j] += d[j-i]
print(d[k])