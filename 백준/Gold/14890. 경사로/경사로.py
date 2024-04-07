import sys

input = sys.stdin.readline


# 길을 지나가는 조건
# 1. 모든 칸의 높이가 같다
# 2. 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
# 경사로 높이는 항상 1, 길이는 l 개수는 많다
# 사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.

def check(a, l):
    flag = False
    visited = [0] * n

    for i in range(n - 1):
        # 같다면 진행시켜
        if a[i] == a[i + 1]:
            continue
        # 높이가 1보다 많이 차이나면
        # 불가능하다
        elif abs(a[i] - a[i + 1]) > 1:
            flag = False
            return flag
        # 왼쪽이 한 칸 더 크다면
        elif a[i] > a[i + 1]:
            standard = a[i + 1]
            # 뒤에 더 조사
            for j in range(i + 1, i + l + 1):
                if 0 <= j < n:
                    if a[j] != standard:
                        flag = False
                        return flag
                    elif visited[j] == 1:
                        flag = False
                        return flag
                    else:
                        visited[j] = 1
                else:
                    flag = False
                    return flag
        elif a[i] < a[i + 1]:
            standard = a[i]
            # 앞에 더 조사
            for j in range(i+1 - l, i+1):
                if 0 <= j < n:
                    if a[j] != standard:
                        flag = False
                        return flag
                    elif visited[j] == 1:
                        flag = False
                        return flag
                    else:
                        visited[j] = 1
                else:
                    flag = False
                    return flag
    flag = True
    return flag


n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    if check(arr[i], l):
        # print(arr[i])
        result += 1
    # print(check(arr[i], l))

for i in range(n):
    new = []
    for j in range(n):
        new.append(arr[j][i])

    if check(new, l):
        # print(new)
        result += 1

print(result)
