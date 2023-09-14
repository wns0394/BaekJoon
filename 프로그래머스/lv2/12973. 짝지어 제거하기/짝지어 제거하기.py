from collections import deque

def solution(s):
    answer = -1
    
    q = deque()
    for i in range(len(s)):
        if len(q) >0 and s[i] == q[-1]:
            q.pop()
        else:
            q.append(s[i])
    if q:
        answer = 0
    else:
        answer = 1

    return answer