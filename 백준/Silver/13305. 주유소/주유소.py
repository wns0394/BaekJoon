import sys

input = sys.stdin.readline

n = int(input())

distance = list(map(int, input().split()))

price = list(map(int, input().split()))

result = price[0] * distance[0]

x = price[0]

for i in range(1, n - 1):
    if x > price[i]:
        x = price[i]
    result += x * distance[i]

print(result)
