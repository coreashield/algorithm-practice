def solution(my_string, is_prefix):
    answer = 0
    
    length = len(is_prefix)
    check_word = my_string[:length]
    if check_word == is_prefix:
        answer = 1
    else :
        answer = 0
    
    return answer