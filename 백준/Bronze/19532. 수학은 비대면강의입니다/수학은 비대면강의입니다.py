a, b, c, d, e, f = map(int, input().split())

x = 0
y = 0
if a == 0:
    y = c / b
    x = (f - e*y) / d
elif b == 0:
    x = c / a
    y = (f - e*x) / d
elif d == 0:
    y = f / e
    x = (c-b*y) / a
elif e == 0:
    x = f / d
    y = (c-a*x) / b
elif a == d:
    y = (c - f) / (b - e)
    x = (c - b * y) / a
elif b == e:
    x = (c - f) / (a - d)
    y = (c - a * x) / b

elif a != d:
    y = (c * d - f * a) / (b * d - e * a)
    x = (c - b * y) / a
print(int(x), int(y))