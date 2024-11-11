def solution(myString, pat):
    myString = myString.replace("A","C").replace("B","A").replace("C","B")
    return int(pat in myString)