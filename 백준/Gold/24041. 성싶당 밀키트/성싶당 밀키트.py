import sys

input = sys.stdin.readline

n, g, k = map(int, input().split())

arr = []

# 구매 후 x일에 i번째 재료에 있는 세균수
# s_i * max(1,x-l_i)

for _ in range(n):
    s, l, o = map(int, input().split())
    arr.append((s, l, o))

s = 1
e = int(2e9)
result = 0

while s <= e:
    virus = 0

    mid = (s + e) // 2
    count = 0
    arr.sort(key=lambda x: (-x[0] * max(1,mid - x[1])))

    for i in range(n):
        if arr[i][2] == 1 and count < k:
            count += 1
        else:
            virus += arr[i][0] * max(1, mid - arr[i][1])


    if virus <= g:
        result = max(result,mid)
        s = mid + 1
    else:
        e = mid - 1

print(result)
