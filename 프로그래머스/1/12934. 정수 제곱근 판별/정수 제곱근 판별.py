def solution(n):
    n = int(n)
    answer = -1
    for i in range(n+1):
        if i * i == n:
            return int((i+1)*(i+1))
    return answer