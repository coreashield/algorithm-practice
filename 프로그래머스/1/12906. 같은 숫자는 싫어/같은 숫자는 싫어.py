def solution(arr):
    answer = []
    past_no = 0
    for idx in range(len(arr)):
        if idx == 0:
            past_no = arr[idx]
            answer.append(past_no)
        elif past_no != arr[idx]:
            answer.append(arr[idx])
            past_no = arr[idx]
            continue
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print( )
    return answer