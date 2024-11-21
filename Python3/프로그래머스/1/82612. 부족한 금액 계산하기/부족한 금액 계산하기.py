def solution(price, money, count):
    answer = price
    for i in range(2,count+1):
        answer += (price * i)
        print(answer)
#     부족하지 않음
    if answer <= money : 
        answer = 0
    else:
        answer -= money
    return answer