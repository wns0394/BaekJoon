n = int(input())
arr = list(map(int, input().split()))

# d[i] - > i개의 카드로 최대값
d = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i+1):
        d[i] = max(d[i], d[i - j] + arr[j-1])
print(d[n])
# d[0] = 0
# d[1] = 1
# d[2] = 5
# d[3] = 6
# d[4] = 10
# d[5] = 11

# 1개로 만들 수 있는 경우 1
# 2 -> 1+1 or 5
# 3 -> 1+1+1 or 5+1
# 4 -> 1+1+1+1 or 5+5 or 1+6

# i개로 만드는거중에서 최대는
# i-1개에서 1개 추가하는거 i-2개에서 2개 추가하는거 i-3개에서 3개추가하는거..... 중  가장 큰 값
