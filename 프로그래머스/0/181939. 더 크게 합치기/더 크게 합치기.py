def solution(a, b):
    answer = 0
    sum1 = str(a) + str(b)
    sum2 = str(b) + str(a)
    
    if sum1 > sum2:
        return int(sum1)
    elif sum2 > sum1:
        return int(sum2)
    else :
        return int(sum1)
    