def solution(s):
    answer = 1001
    
    # 압축 제일 많이 해도 절반 이므로 
    # i는 압축 길이
    for i in range(1, len(s) + 1):
        x = s[0:i]
        result = ''
        num = 1
        # i부터 끝까지 압축길이 만큼 조사 
        for j in range(i, len(s), i):
            # 압축한거랑 같으면 num 증가
            if x == s[j:j+i]:
                num += 1
            # 다르면 
            else:
                if num != 1:
                    result += str(num)  
                result += x
                x = s[j:j+i]
                num = 1
        if x:
            if num != 1:
                result += str(num)
            result += x
        answer = min(answer, len(result))
    return answer