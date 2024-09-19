class Solution {
    fun solution(n: Int): Int {
        for(i in 0..n/2)
            if(i*i == n){
                return 1     
            }
        return 2
    }
}

// x제곱 = n인지 확인
