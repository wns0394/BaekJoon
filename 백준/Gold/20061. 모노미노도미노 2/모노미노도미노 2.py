
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


def remove(arr, i):
    for a in range(i, 0, -1):
        for b in range(4):
            arr[a][b] = arr[a - 1][b]
    for j in range(4):
        arr[0][j] = 0

n = int(input())

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

result = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    drop_green(t, y)

    drop_blue(t, x)

    for i in range(2, 6):
        g_cnt = 0
        b_cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                g_cnt += 1
            if blue[i][j] == 1:
                b_cnt += 1
        if g_cnt == 4:
            remove(green, i)
            result += 1
        if b_cnt == 4:
            remove(blue, i)
            result += 1

    green_count = 0
    blue_count = 0
    for i in range(2):
        if 1 in green[i]:
            green_count += 1
        if 1 in blue[i]:
            blue_count += 1

    if green_count:
        while green_count > 0:
            remove(green, 5)
            green_count -= 1

    if blue_count:
        while blue_count > 0:
            remove(blue, 5)
            blue_count -= 1

print(result)

count = 0
for i in range(6):
    for j in range(4):
        if blue[i][j] == 1:
            count += 1
        if green[i][j] == 1:
            count += 1

print(count)
