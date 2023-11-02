n = int(input())


for _ in range(n):
    a = int(input())
    d = [1,1,1,2,2] + [0] * a
    for i in range(5,a+1):
        d[i] = d[i-1] + d[i-5]

    print(d[a-1])