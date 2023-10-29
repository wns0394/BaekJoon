n = int(input())

arr = list(map(int,input().split()))

s = 0
e = n-1
result = 0

while s < e:

    result = max(result,(e-s-1)*min(arr[s],arr[e]))

    # s를 1더하든 e를 1 빼든 사이에 존재하는 개발자 수는 똑같다
    # 그렇다면 min값을 늘려야하기 때문에 작은애를 당겨준다.
    if arr[s] < arr[e]:
        s += 1
    else:
        e -= 1

print(result)