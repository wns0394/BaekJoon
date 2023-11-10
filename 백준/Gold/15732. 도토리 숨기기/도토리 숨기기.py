# n 상자의 수 1 <= n <= 1000000
# k 규칙의 수 1 <= k <= 100000
# d 도토리 수 1 <= d <= 1000000000
# -> 완전탐색 절대 불가능 그러면? 이분탐색?
n, k, d = map(int, input().split())

start = 0
end = n

arr = []
for _ in range(k):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))


while start <= end:

    result = 0

    mid = (start + end) // 2

    for x, y, z in arr:
        if x > mid:
            continue
        result += (min(mid,y) - x) // z + 1

    if result >= d:
        end = mid-1
    else:
        start = mid + 1

print(start)
