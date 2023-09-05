arr = list(input())

stack = []

result = ''

for i in arr:
    if i.isalpha() == True:
        result += i
    else:
        # 여는 괄호는
        if i == '(':
            # 그냥 추가
            stack.append(i)
        # 닫는 괄호라면
        elif i == ')':
            # 스택이 존재하고 여는 괄호를 만날때까지
            while stack and stack[-1] != '(':
                # 안에있는 사칙연산을 더해준다.
                result += stack.pop()
            # 여는 괄호를 삭제
            stack.pop()
        # 곱하기나 나누기라면
        elif i == '*' or i == '/':
            # +,-가 마지막이라면 *나 /를 먼저 계산하므로
            # 스택이 존재하고 마지막이 +,-가 아니라면 result에 추가
            while stack and stack[-1] != '+' and stack[-1] != '-' and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        # +,- 라면
        elif i == '+' or i == '-':
            # 스택이 존재하고 여는괄호가 아니라면
            # 결과값에 스택들을 추가
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
while stack:
    result += stack.pop()
print(result)