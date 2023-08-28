
n = int(input())

arr = list(map(int, input().split()))

arr.sort()
s = 0
e = n-1
mini = arr[s] + arr[e]
while s < e:
    result = arr[s] + arr[e]
    # 더한값이 0이라면
    if result == 0:
        mini = 0
        break
    if abs(result) < abs(mini):
        mini = result
    # 합이 음수가되면 합의 절대값이 더 커지므로 s를 1 증가한다
    if result < 0:
        s += 1
    # 합이 양수라면 합의 절대값을 줄이기위해 e를 1 감소
    else:
        e -= 1
print(mini)