def solution(spell, dic):
    answer = 2
    for i in dic:
        spell_cnt = 0
        for j in spell:
            if j in i:
                spell_cnt += 1
        if len(spell) == spell_cnt:
            answer = 1
            
    return answer


# dic의 요소를 하나씩 꺼낸다.(i)
# 변수 i에 spell에 있는 알파벳 j가 들어있는지 확인한다.
# 들어가있다면 해당 알파펫 카운트도 카운팅한다.
# 1개씩 모두 들어가있다면 answer + 1
