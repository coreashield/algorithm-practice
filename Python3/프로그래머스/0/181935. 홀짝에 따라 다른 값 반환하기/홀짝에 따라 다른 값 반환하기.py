def solution(n):
    answer = 0
    if n % 2 == 0:
        start_num = 2
    else:
        start_num = 1
    for i in range(start_num,n+1,2):
        if start_num == 2:
            answer += (i * i) 
        else:
            answer += i
    return answer