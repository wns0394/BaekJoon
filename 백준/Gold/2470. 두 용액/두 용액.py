n = int(input())

arr = list(map(int, input().split()))

arr.sort()
s = 0
e = n - 1

mini = arr[s] + arr[e]
two = [arr[s],arr[e]]
while s < e:
    result = arr[s] + arr[e]

    if result == 0:
        two = [arr[s],arr[e]]
        break
    # result값이 더 0에 가깝다면
    if abs(result) < abs(mini):
        mini = result
        two = [arr[s],arr[e]]
    if result < 0:
        s += 1

    if result > 0:
        e -= 1
print(*two)