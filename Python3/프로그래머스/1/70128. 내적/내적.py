def solution(a, b):
    answer = 0
    for a_value, b_value in zip(a,b):
        answer += a_value * b_value
    return answer