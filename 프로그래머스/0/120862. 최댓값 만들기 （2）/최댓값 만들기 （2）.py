def solution(numbers):
        
    max_product = numbers[0] * numbers[1]  # 초기값 설정
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            product = numbers[i] * numbers[j]
            max_product = max(max_product, product)
    
    return max_product