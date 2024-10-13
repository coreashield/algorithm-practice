def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        answer.append(num_list[i])
        if i == len(num_list)-1:
            if num_list[i-1] < num_list[i]:
                answer.append(num_list[i] - num_list[i-1])
            else:
                answer.append(num_list[i] * 2)
                    
            
    
        
    return answer