c, p = map(int, input().split())

arr = list(map(int, input().split()))

result = 0

# 길쭉한모양
if p == 1:
    # 세워서 모든 열에 다 가능하므로
    result += c
    for i in range(3, c):
        if arr[i - 3] == arr[i - 2] and arr[i - 3] == arr[i - 1] and arr[i - 3] == arr[i]:
            result += 1

elif p == 2:
    for i in range(1, c):
        if arr[i - 1] == arr[i]:
            result += 1

elif p == 3:
    for i in range(2, c):
        if arr[i - 2] == arr[i - 1] and arr[i - 1] == arr[i] - 1:
            result += 1
        if arr[i - 1] - 1 == arr[i]:
            result += 1
    if arr[0] - 1 == arr[1]:
        result += 1

elif p == 4:
    for i in range(2, c):
        if arr[i - 2] - 1 == arr[i - 1] and arr[i - 1] == arr[i]:
            result += 1
        if arr[i - 1] == arr[i] - 1:
            result += 1
    if arr[0] == arr[1] - 1:
        result += 1

elif p == 5:
    for i in range(2, c):
        if arr[i - 2] == arr[i - 1] and arr[i - 2] == arr[i]:
            result += 1
        if arr[i - 2] - 1 == arr[i - 1]:
            result += 1
        if arr[i - 1] == arr[i] - 1:
            result += 1
        if arr[i - 2] - 1 == arr[i - 1] and arr[i - 1] == arr[i] - 1:
            result += 1

elif p == 6:
    for i in range(1, c):
        if arr[i - 1] == arr[i]:
            result += 1
        if i >= 2 and arr[i - 2] == arr[i - 1] and arr[i - 2] == arr[i]:
            result += 1
        if i >= 2 and arr[i - 2] == arr[i - 1] - 1 and arr[i - 1] == arr[i]:
            result += 1
        if arr[i - 1] - 2 == arr[i]:
            result += 1

elif p == 7:
    for i in range(1, c):
        if arr[i - 1] == arr[i]:
            result += 1
        if i >= 2 and arr[i - 2] == arr[i - 1] and arr[i - 2] == arr[i]:
            result += 1
        if i >= 2 and arr[i - 2] == arr[i - 1] and arr[i - 1] - 1 == arr[i]:
            result += 1
        if arr[i - 1] == arr[i] - 2:
            result += 1
print(result)
