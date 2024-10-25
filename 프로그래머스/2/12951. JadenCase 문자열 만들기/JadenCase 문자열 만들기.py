def solution(s):
    answer = ''
    # a = s.split()
    # for i in range(0,len(a)):
    #     a[i] = a[i].lower()
    #     answer += a[i].capitalize()
    #     if i > 0 :
    #         answer += " "
    word = ""
    for i in s:
        if i != " ":
            word += i
        else:
            answer += word.capitalize() + " "
            word = ""
    answer += word.capitalize()
    return answer