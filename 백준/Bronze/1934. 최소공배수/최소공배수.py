def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    # 최대 공배수
    gcd(a,b)
    print(int((a*b)/gcd(a,b)))