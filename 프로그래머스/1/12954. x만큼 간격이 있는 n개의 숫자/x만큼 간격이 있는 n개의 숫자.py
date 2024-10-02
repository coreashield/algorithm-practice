def solution(x, n):
    answer = []
    start_no = x
    
    for _ in range(n):  # n번 반복
        answer.append(start_no)
        start_no += x  # x만큼 값을 더함
    
    return answer