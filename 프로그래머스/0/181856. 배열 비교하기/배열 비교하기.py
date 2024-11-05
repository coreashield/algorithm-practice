def solution(arr1, arr2):
    answer = 0
    
    if len(arr1) > len(arr2) :
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        for i in arr1:
            answer += i
        for i in arr2:
            answer -= i
        if answer > 0 :
            return 1
        elif answer < 0:
            return -1
        else:
            return 0
        
    return answer