def solution(str1, str2):
    
    answer = str1.find(str2)
    if answer > -1:
        return 1
    else:
        return 2