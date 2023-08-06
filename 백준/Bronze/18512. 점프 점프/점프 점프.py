x,y,p1,p2 = map(int,input().split())
cnt = 0
while True:
    if p1 == p2:
        break
    if p1 > p2:
        p2 += y
    elif p1 < p2:
        p1 += x
    if cnt > 100000:
        p1 = -1
        break
    cnt += 1

print(p1)