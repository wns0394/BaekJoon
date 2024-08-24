import sys

from pprint import pprint

input = sys.stdin.readline


def check(x):
    # print(x)
    # 부품을 이미 체크 한 적이 있다면
    if visited[x][0] != -1:
        # print(x,'이미 처리함')
        # x를 이루는 기본 부품들 반환
        return visited[x]

    # x번의 부품을 확인하기 위해 초기화
    visited[x] = [0] * (n + 1)

    # 기본 부품인지 확인하기 위한 flag
    flag = True

    # 기본 부품이려면 모두 0이여야한다.
    for i in range(1, n + 1):
        # 만약 다른 부품으로 이루어져있다면
        # 중간 부품이다
        if arr[x][i] > 0:
            # flag False
            flag = False
            break

    # 기본 부품이라면
    if flag:
        # x는 x로 이루어져있다.
        # print(x,'기본부품')
        visited[x][x] = 1
        return visited[x]

    # x번의 부품들 중에서
    for i in range(n - 1, 0, -1):
        # i번의 부품이 있다면
        if arr[x][i] > 0:
            # i번 부품에 대해서 다시 체크
            a = check(i)
            # x번의 부품을 업데이트
            for j in range(1, n + 1):
                visited[x][j] += a[j] * arr[x][i]
    # print(visited[x],x)
    return visited[x]


n = int(input())
m = int(input())

arr = [[0] * (n + 1) for _ in range(n + 1)]

# visited[i][j] -> i 를 이루는데 필요한 기본부품 j의 수
# 즉 우리가 구하고자하는
# visited[n]에서 0보다 큰 아이들을 구하면 필요한 기본부품의 수가 나온다.
visited = [[-1] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    # x를 만드는데 y가 k개 필요하다.
    x, y, k = map(int, input().split())
    arr[x][y] = k

# n번을 체크한다.
check(n)

# print(visited[n])

for i in range(1,n+1):
    if visited[n][i] > 0:
        print(i, visited[n][i])
