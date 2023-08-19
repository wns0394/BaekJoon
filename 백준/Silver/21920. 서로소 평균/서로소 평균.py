def gcd(x, y):
    if x < y:
        x, y = y, x

    while y != 0:
        x, y = y, x % y
    return x


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

result = []

for i in arr:
    if gcd(i,m) == 1:
        result.append(i)
print(sum(result)/len(result))