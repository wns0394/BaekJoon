def solution(s):
    answer = 1001
    # 압축은 절반까지만 될것이다
    result = []
    # 자르는 개수 i
    
    if len(s) == 1:
        answer = 1
    else:
        for i in range(1,len(s)//2+1):
            x = ""
            y = s[0:i]
            count = 1

            for j in range(i, len(s) + i, i):
                if y == s[j:j+i]:
                    count += 1
                else:
                    if count != 1:
                        x = x + str(count) + y
                    else:
                        x = x + y

                    y = s[j:j+i]
                    count = 1
            result.append(len(x))
        m = min(result)
        answer = min(answer,m)
    return answer