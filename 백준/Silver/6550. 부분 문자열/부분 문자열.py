import sys
from collections import deque

for a in sys.stdin:
    s,t = a.split()
    q = deque(list(s))
    for i in t:

        if q and i == q[0]:
            q.popleft()
    if q:
        print('No')
    else:
        print('Yes')