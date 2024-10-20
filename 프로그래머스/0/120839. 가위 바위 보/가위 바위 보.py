def solution(rsp):
    rsp = rsp.replace("0","바위")
    rsp = rsp.replace("5","보")
    rsp = rsp.replace("2","가위")
    
    return rsp.replace("바위","5").replace("보","2").replace("가위","0")