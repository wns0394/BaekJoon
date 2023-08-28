n = int(input())

arr = list(map(int, input().split()))

d = [0] * (1001)

for i in range(n):
    for j in range(i):
        # 감소하고있고 i번째 합이 j번째 합보다 작다면
        if arr[i] < arr[j] and d[i] < d[j]:
            d[i] = d[j]
    # 현재값 더해주기
    d[i] += arr[i]
print(max(d))