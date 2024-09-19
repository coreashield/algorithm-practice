def solution(s):
    r = list(map(int, s.split()))
    max_val = max(r)
    min_val = min(r)
    
    return f"{min_val} {max_val}"