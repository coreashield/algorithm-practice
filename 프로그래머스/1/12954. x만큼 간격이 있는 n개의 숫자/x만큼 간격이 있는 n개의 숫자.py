def solution(x, n):
    answer = []
    answer_cnt = 0
    start_no = x
    
    while(answer_cnt < n):
        answer.append(start_no)
        start_no += x
        answer_cnt += 1
    return answer