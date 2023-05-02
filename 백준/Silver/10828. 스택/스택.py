import sys
n = int(input())
stack = []
for _ in range(n):
    a = sys.stdin.readline()
    if a.split()[0] == 'push':
        stack.append(a.split()[1])
    elif a.split()[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif a.split()[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif a.split()[0] == 'size':
        print(len(stack))
    elif a.split()[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)