import sys

input = sys.stdin.readline

from pprint import pprint

r1, c1, r2, c2 = map(int, input().split())

x = r2 - r1 + 1
y = c2 - c1 + 1


# (-a, -a)
# 1 5 17 37 65 101
#  4 12 20 28 36

# 0 -> 1 + (4*0)
# 1 -> 1 + (4*1)
# 2 -> 5 + (4*3) = 1 + (4*1) + (4*3) = 1 + 4 * 4
# 3 -> 17 + (4*5) =  1 + (4*1) + (4*3) + (4*5) = 1 + 4* 9
# 4 -> 37 + (4*7) = 1 + (4*1) + (4*3) + (4*5)+ (4*7) = 1 + 4* 16
# 1 + 4*n^2

# (-a,a)
# (-a,-a)
# 1 5 17 37 65 = 4*n^2 + 1
# 1 3 13 31 57 = 4*n^2 - 2*n + 1
# 0 2  4  6  8

# (-a,a)
# (-a,-a)
# 1 7 21 43 73 = 4*n^2 + 2*n + 1
# 1 5 17 37 65 = 4*n^2 + 1
# 0 2 4  6  8

# (a,a)
# (-a,a)
# 1 9 25 49 81 = 4*n^2 + 4*n + 1
# 1 3 13 31 57 = 4*n^2 - 2*n + 1
# 0 6 12 18 24

# 구역을 나누자
# ▽ # (-a,-a)에서 빼주자 1구역
# -1 -1 -1 0 -1 1
# -2 -1 -2 0 -2 1
# ▷ # (-a,-a)에서 더해주자 2구역
# △ # (a,a)에서 빼주자 # 3구역
# ◁ # (-a,a)에서 빼주자 # 4구역

# (x,y)가 나왔을때 어느 구역인지 정하는 방법법

arr = [[0] * y for _ in range(x)]
max_len = 0
for i in range(x):
    for j in range(y):
        a = i + r1
        b = j + c1
        if abs(a) == abs(b):
            if a > 0 and b > 0:
                arr[i][j] = 4 * (a ** 2) + 4 * a + 1
            if a > 0 and b < 0:
                arr[i][j] = 4 * (a ** 2) + 2 * a + 1
            if a < 0 and b < 0:
                arr[i][j] = 4 * (abs(a) ** 2) + 1
            if a < 0 and b > 0:
                arr[i][j] = 4 * (abs(a) ** 2) - 2 * abs(a) + 1
            if a == 0 and b == 0:
                arr[i][j] = 1
        else:
            if a < 0 and abs(a) > abs(b):
                arr[i][j] = 4 * (abs(a) ** 2) + 1 - (b - a)
            if b < 0 and abs(a) < abs(b):
                arr[i][j] = 4 * (abs(b) ** 2) + 1 + (a - b)
            if a > 0 and abs(a) > abs(b):
                arr[i][j] = 4 * (a ** 2) + 4 * a + 1 - (a - b)
            if b > 0 and abs(a) < abs(b):
                arr[i][j] = 4 * (b ** 2) - 2 * b + 1 - (b + a)
        if len(str(arr[i][j])) > max_len:
            max_len = len(str(arr[i][j]))
# print(max_len)
for i in range(x):
    for j in range(y):
        if len(str(arr[i][j])) < max_len:
            print(str(arr[i][j]).rjust(max_len,' '), end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
