import sys


from pprint import pprint

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]

result = 1000000000

for sx in range(0, n - 7):
    for sy in range(0, m - 7):

        count = 0
        count2 = 0
        for ex in range(sx, sx + 8):
            for ey in range(sy, sy + 8):

                if (ex + ey) % 2 == (sx + sy) % 2 and arr[sx][sy] != arr[ex][ey]:
                    count += 1
                elif (ex + ey) % 2 != (sx + sy) % 2 and arr[sx][sy] == arr[ex][ey]:
                    count += 1
                if (ex + ey) % 2 == (sx + sy) % 2 and arr[sx][sy] == arr[ex][ey]:
                    count2 += 1
                elif (ex + ey) % 2 != (sx + sy) % 2 and arr[sx][sy] != arr[ex][ey]:
                    count2 += 1
        result = min(count, result, count2)

print(result)
