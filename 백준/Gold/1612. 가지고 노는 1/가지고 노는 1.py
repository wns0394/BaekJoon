n = int(input())

a = 11
count = 2
# n으로 나누었을때 나머지가 0이다.
# 11, 111, 1111, 11111, 111111 .....
# 2의배수 or 5의 배수라면
# 1이 나올 수 없다
if n % 2 == 0 or n % 5 == 0:
    print(-1)
elif n == 1:
    print(1)
else:
    while a % n != 0:
        a = a % n
        a = a * 10 + 1
        count += 1
    print(count)