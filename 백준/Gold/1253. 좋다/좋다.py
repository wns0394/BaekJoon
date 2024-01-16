import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

set_arr = set(arr)

result = 0

for i in range(n):

    s = 0
    e = n-1

    while s < e:
        if arr[s] + arr[e] == arr[i]:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                result += 1
                break
        elif arr[s] + arr[e] > arr[i]:
            e -= 1
        else:
            s += 1

print(result)