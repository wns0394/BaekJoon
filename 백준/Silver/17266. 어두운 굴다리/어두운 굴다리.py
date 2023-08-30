# 굴다리 길이 n
n = int(input())
# 가로등 개수 m
m = int(input())

arr = list(map(int, input().split()))

result = 0

# 가로등이 하나라면
# 왼쪽 오른쪽 중 먼곳의 높이
if m == 1:
    result = max(arr[0], n - arr[0])

else:
    for i in range(m):
        # 처음 가로등
        if i == 0:
            x = arr[i]
        # 마지막 가로등
        elif i == m-1:
            x = n - arr[i]
        # 중간에 있는 가로등들
        # 옆에 가로등과의 거리의 절반반 비추면된다.
        else:
            distance = arr[i] - arr[i-1]

            # 거리가 2의 배수 ex) 4라면 2씩 비추면된다
            if distance % 2 == 0:
                x = distance // 2
            # 거리가 홀수라면 ex) 5 -> 2씩 비추면 모자란다
            else:
                x = distance // 2 + 1
        result = max(x,result)

print(result)