t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    # d[i] => i원을 만드는 방법의 개수
    d = [0] * (m + 1)
    d[0] = 1
    for i in coin:
        for j in range(i,m+1):
            # j원을 만드는 방법은
            # i원을 더해서 만들수 있는거만큼 더해준다 
            d[j] += d[j-i]
    print(d[m])