import sys
from collections import deque
n = int(input())
deque = deque()

for _ in range(n):
    a = sys.stdin.readline()
    if a.split()[0] == 'push_front':
        deque.appendleft(a.split()[1])
    if a.split()[0] == 'push_back':
        deque.append(a.split()[1])
    elif a.split()[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.popleft()
    elif a.split()[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif a.split()[0] == 'size':
        print(len(deque))
    elif a.split()[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif a.split()[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif a.split()[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])