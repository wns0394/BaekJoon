def solution(words, queries):
    head, head_rev = {}, {}
    wc = []
    
    def add(head,word):
        node = head
        # 단어에서 문자하나
        for w in word:
            # 그 문자가 node의 키에 존재하지 않는다면
            if w not in node:
                # 노드의 키에 문자를 추가하고 값으로 dict를 넣어줌
                node[w]={}
            
            node= node[w]
            # len이라는 키워드가 없으면
            if 'len' not in node:
                # len키를 가진 리스트를 생성하고 길이를 넣는다
                node['len'] = [len_word]
            # len 키워드가 있으면
            else:
                # 리스트에 문자열의 길이 넣어준다
                node['len'].append(len_word)
        # 끝났다는 표시인 end를 넣어준다
        node['end']=True   
        
    
    for word in words:
        len_word = len(word)
        add(head,word)
        add(head_rev,word[::-1])
        wc.append(len_word)
    
    # search 함수
    def search(head, querie):
        0
        node = head
        for q in querie:
            if q=='?':
                return node['len'].count(len(querie))
            elif q not in node:
                break
            node = node[q]
        return 0
    
    answer = []
    
    for q in queries:
        # 시작이 ?라면 
        # 뒤집은거 조사
        if q[0] == '?':
            if q[-1] == "?":
                answer.append(wc.count(len(q)))
            else:
                answer.append(search(head_rev,q[::-1]))
        # 끝이 ?라면
        # 그대로 조사
        else:
            answer.append(search(head,q))
    
    return answer