def solution(arr):
    answer = []
    if len(arr) < 2 :
        return [-1]
    min_no = min(arr)
    for i in arr:
        if i != min_no:
            answer.append(i)
    return answer