from copy import deepcopy

def drop_green(t, y):
    x = 6

    if t == 1:
        for i in range(6):
            if green[i][y] == 1:
                x = i
                break
        green[x - 1][y] = 1

    elif t == 3:
        for i in range(6):
            if green[i][y] == 1:
                x = i
                break
        green[x - 1][y] = 1
        green[x - 2][y] = 1

    elif t == 2:
        for i in range(6):
            if green[i][y] == 1 or green[i][y + 1] == 1:
                x = i
                break

        green[x - 1][y] = 1
        green[x - 1][y + 1] = 1


def drop_blue(t, x):
    new_x = 6
    new_y = 3 - x
    if t == 1:
        for i in range(6):
            if blue[i][new_y] == 1:
                new_x = i
                break
        blue[new_x - 1][new_y] = 1

    elif t == 2:
        for i in range(6):
            if blue[i][new_y] == 1:
                new_x = i
                break
        blue[new_x - 1][new_y] = 1
        blue[new_x - 2][new_y] = 1

    elif t == 3:
        for i in range(6):
            if blue[i][new_y] or blue[i][new_y - 1] == 1:
                new_x = i
                break
        blue[new_x - 1][new_y] = 1
        blue[new_x - 1][new_y - 1] = 1


n = int(input())

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

result = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    # print(t, x, y)
    # for i in range(6):
    #     print(*green[i], '시작')
    # print('------------------')

    drop_green(t, y)

    drop_blue(t, x)

    # for i in range(6):
    #     print(*green[i], '드롭시킨후')
    # print('---------------------')

    for i in range(6):
        if green[i] == [1, 1, 1, 1]:
            for j in range(i, 0, -1):
                green[j] = deepcopy(green[j - 1])
            result += 1
        if blue[i] == [1, 1, 1, 1]:
            for j in range(i, 0, -1):
                blue[j] = deepcopy(blue[j - 1])
            result += 1

    # for i in range(6):
    #     print(*green[i], '1줄 삭제')
    # print('---------------------')
    green_count = 0
    blue_count = 0
    for i in range(2):
        if 1 in green[i]:
            green_count += 1
        if 1 in blue[i]:
            blue_count += 1

    if green_count:
        if green_count == 1:
            green[5] = [0, 0, 0, 0]

            for i in range(4, -1, -1):
                green[i + 1] = green[i]
            green[1] = [0, 0, 0, 0]

        elif green_count == 2:
            green[5] = [0, 0, 0, 0]
            green[4] = [0, 0, 0, 0]

            for i in range(3, -1, -1):
                green[i + 2] = green[i]
            green[0] = [0, 0, 0, 0]
            green[1] = [0, 0, 0, 0]

    if blue_count:
        if blue_count == 1:
            blue[5] = [0, 0, 0, 0]

            for i in range(4, -1, -1):
                blue[i + 1] = blue[i]
            blue[1] = [0, 0, 0, 0]

        elif blue_count == 2:
            blue[5] = [0, 0, 0, 0]
            blue[4] = [0, 0, 0, 0]

            for i in range(3, -1, -1):
                blue[i + 2] = blue[i]
            blue[0] = [0, 0, 0, 0]
            blue[1] = [0, 0, 0, 0]

    # for i in range(6):
    #     print(*green[i], '위에줄 침범')
    # print('---------------------')

print(result)

count = 0
for i in range(6):
    for j in range(4):
        if blue[i][j] == 1:
            count += 1
        if green[i][j] == 1:
            count += 1
print(count)
