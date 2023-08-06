import sys
n = int(input())
minus = []
plus = []
zero = []
for _ in range(n):
    a = int(input())
    if a < 0:
        minus.append(a)
    elif a > 0:
        plus.append(a)
    else:
        zero.append(a)
minus.sort()
plus.sort(reverse=True)
# 음수의 개수가 짝수이면 모두 곱한다.
# 음수의 개수가 홀수이면 제일 작은거 빼고 서로 곱한다.
# 양수의 개수가 짝수이면 모두 곱한다.
# 양수의 개수가 홀수이면 제일 작은거 빼고 서로 곱한다.
# 0이 있고 음수가 한개 있으면 서로 곱한다. 아니면 그냥 둔다.
# 마지막이 1,1 두개라면 안곱하고 더한다!!
# 예제 아니였으면 몰랐을듯 예외처리에 신경쓰자
# 마지막이 1이면 곱하는게 별로다 더하자
# 이거는 짝수개이나 홀수개이나 마찬가지
result = 0
if len(minus) % 2 == 0:
    for i in range(0,len(minus),2):
        result += minus[i] * minus[i+1]
else:
    for i in range(0,len(minus)-1,2):
        result += minus[i] * minus[i+1]
    if zero:
        result += 0
    else:
        result += minus[-1]

if len(plus) % 2 == 0:
    for i in range(0,len(plus),2):
        if plus[i+1] == 1:
            result += plus[i] + plus[i+1]
        else:
            result += plus[i] * plus[i+1]
else:
    for i in range(0,len(plus)-1,2):
        if plus[i+1] == 1:
            result += plus[i] + plus[i+1]
        else:
            result += plus[i] * plus[i+1]
    result += plus[-1]
print(result)