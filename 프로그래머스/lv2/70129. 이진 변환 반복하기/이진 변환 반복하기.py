
def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0
    s_list = list(s)
    new = bin(s_list.count('1'))
    while s_list != ['1']:
        new = bin(s_list.count('1'))
        zero_cnt += s_list.count('0')
        cnt += 1
        s_list = list(new)[2::]
        
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer