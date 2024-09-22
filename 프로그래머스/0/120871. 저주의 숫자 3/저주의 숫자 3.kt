class Solution {
    fun solution(n: Int): Int {
        var answer = 1 // 1부터 시작
        var count = 0  // 유효한 숫자들을 세는 변수

        do {
            // 3의 배수이거나 숫자에 '3'이 포함되면 건너뜀
            if (answer % 3 != 0 && !answer.toString().contains('3')) {
                count++ // 유효한 숫자만 카운트 증가
            }
            answer++
        } while (count < n) // 유효한 숫자 n개가 나올 때까지 반복
        
        return answer - 1 // 마지막에 증가한 값을 보정하여 반환
    }
}
