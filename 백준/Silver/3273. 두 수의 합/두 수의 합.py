n = int(input())

arr = list(map(int, input().split()))
arr.sort()
x = int(input())

s = 0
e = n-1

cnt = 0
while s < e:
    result = arr[s] + arr[e]
    if result == x:
        s += 1
        cnt += 1
    elif result < x:
        s += 1
    elif result > x:
        e -= 1
print(cnt)