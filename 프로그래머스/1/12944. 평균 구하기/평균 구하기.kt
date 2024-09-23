class Solution {
    fun solution(arr: IntArray): Double {
        var answer: Double = 0.0
        var length = arr.size
        for(i in arr.indices){
            answer += arr[i]
        }
        print(answer)
        answer /= length
        return answer
    }
}