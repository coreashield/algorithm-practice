def solution(nums):
    select_cnt = len(nums) / 2
    poketmon_list = []
    poketmon_list.append(nums[0])
    
    for i in range(1,len(nums)):
        if nums[i] in poketmon_list:
            continue
        else:
            poketmon_list.append(nums[i])
            
    if len(poketmon_list) >= select_cnt:
        return select_cnt
    else:
        return len(poketmon_list)
      

# num 길이 / 2 = 포켓몬 선택 수
# 요소를 선택 -> 뒷 요소들과 같다면 리스트에 넣지 않음,