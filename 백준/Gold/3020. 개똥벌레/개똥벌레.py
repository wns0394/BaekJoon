import sys

input = sys.stdin.readline

from bisect import bisect_left

n, h = map(int, input().split())

bottom = []
top = []

for i in range(n):
    a = int(input())
    if i % 2 == 0:
        bottom.append(a)
    else:
        top.append(a)

bottom.sort()
top.sort()

result = 2000001
cnt = 0
for i in range(1, h + 1):
    # 총 부시는 개수
    count = 0

    # 아래 석순을 부수는 개수
    # bisect_left를 하는 이유는 같은 높이일경우 부수는게 가능하므로
    count += (n // 2 - bisect_left(bottom, i))

    # 위 종유석을 부수는 개수
    # 마찬가지로 같은 높이일 경우 부수는게 가능하므로 bisect_left
    count += (n // 2 - bisect_left(top, h + 1 - i))

    # 장애물 부시는 개수가 result보다 작다면 갱신
    if count < result:
        result = count
        # 그러한 구간의 수 + 1
        cnt = 1

    # 최소값과 같다면
    elif count == result:
        # 구간의 수 + 1
        cnt += 1

# 파괴하는 장애물의 최솟값과 그러한 구간의 수 출력
print(result, cnt)
