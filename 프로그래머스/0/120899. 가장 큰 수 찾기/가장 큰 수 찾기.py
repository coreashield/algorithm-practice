def solution(array):
    answer = []
    index = 0
    save_index = 0
    max_no = 0
    for no in array:
        if no > max_no:
            max_no = no
            save_index = index
        index += 1
    answer.append(max_no)
    answer.append(save_index)
    
    return answer