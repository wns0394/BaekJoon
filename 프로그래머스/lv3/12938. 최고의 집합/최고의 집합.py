def solution(n, s):
    answer = []
    
    # 만약 합 s가 n으로 나누어 떨어지면
    # 그 조건을 만족하는 최고의 집합은 [s//n] * n 일것이다.
    if s % n == 0:
        answer.append(s//n)
        answer = answer * n
        return answer
    if n > s:
        answer.append(-1)
        return answer
    else:
        a = s // n
        na = s % n
        answer.append(s//n)
        answer = answer * n
        for i in range(na):
            answer[n-1-i] += 1
    return answer