import sys

input = sys.stdin.readline

from copy import deepcopy

# 방향
# 1,2,3,4 위 아래 왼쪽 오른쪽

# 상하좌우 이동하고 그 칸에 자신의 냄새 뿌림
# 냄새는 K번 이동하고 나면 사라짐

# 이동 방향 결정 순서
# 인접한 칸 중 아무 냄새가 없는 칸의 방향
# 그러한 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 이때 가능한 칸이 여러개일 수 있는데 그 경우 특정한 우선순위를 따른다
# 우선순위는 상어마다 다를 수 있고 같은 상어라도
# 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고
# 그 후에는 방금 이동한 방향이 보고있는 방향이다.

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

shark = [(0, 0) for _ in range(m)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            shark[arr[i][j] - 1] = (i, j)
            arr[i][j] = [arr[i][j], k]
        else:
            arr[i][j] = [0,0]

direction = [0] + list(map(int, input().split()))
# print(direction)
priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

# print(priority)
time = 0
count = m
while True:
    if time > 1000:
        print('-1')
        break
    if count == 1:
        print(time)
        break
    new = deepcopy(arr)

    for i in range(n):
        for j in range(n):
            if new[i][j][1] > 0:
                new[i][j][1] -= 1

    for num in range(m):
        x,y = shark[num]
        if x == -1 and y == -1:
            continue
        # num 번호의 상어 방향
        d = direction[num+1]
        # print(d,num+1)
        # 인접한 칸 중 아무 냄새가 없는 칸이 있는지 확인
        flag = False

        # if x == 2 and y == 0:
        #     print(x,y,d)
        for i in priority[num][d-1]:
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx,ny)
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny][1] == 0:
                    d = i
                    flag = True
                    break

        # 냄새가 다 차있다면
        if flag == False:
            # 자신의 냄새가 차있는곳을 찾아야한다.
            for i in priority[num][d-1]:

                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny][0] == num+1:
                        d = i
                        break
        direction[num+1] = d

        # print(x,y,nx,ny,d,num+1)
        nx = x + dx[d]
        ny = y + dy[d]
        # print(x,y)
        # print(nx,ny,flag)
        # print(nx,ny,num+1,d)
        # 다음 이동장소에 상어가 없다면
        # print(nx,ny,shark,num+1,d)
        if (nx,ny) not in shark:
            new[nx][ny] = [num+1,k]
            shark[num] = (nx,ny)
        # 다음 이동장소에 상어가 있다면
        # 크기 비교
        else:
            if num+1 > new[nx][ny][0]:
                shark[num] = (-1,-1)
            else:
                shark[new[nx][ny][0]] = (-1,-1)
                new[nx][ny] = [num+1,k]
                shark[num] = (nx,ny)
            count -=1
    arr = deepcopy(new)
    time += 1
    # print(time,count)
    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end=' ')
    #     print()
    # print('---------')
