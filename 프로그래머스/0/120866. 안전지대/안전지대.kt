class Solution {
    fun solution(board: Array<IntArray>): Int {
        val n = board.size
        var dangerZone = Array(n) { BooleanArray(n) { false } } // 위험지역을 표시할 배열
        var answer = 0
        
        // 8방향 이동을 위한 좌표
        val dx = arrayOf(-1, -1, -1, 0, 0, 1, 1, 1)
        val dy = arrayOf(-1, 0, 1, -1, 1, -1, 0, 1)
        
        // 지뢰가 있는 곳과 주변을 위험지역으로 표시
        for (i in board.indices) {
            for (j in board[i].indices) {
                if (board[i][j] == 1) {
                    // 현재 지뢰가 있는 칸도 위험지역으로 표시
                    dangerZone[i][j] = true
                    // 8방향으로 위험지역 표시
                    for (k in 0 until 8) {
                        val ni = i + dx[k]
                        val nj = j + dy[k]
                        // 범위를 벗어나지 않도록 체크
                        if (ni in 0 until n && nj in 0 until n) {
                            dangerZone[ni][nj] = true
                        }
                    }
                }
            }
        }
        
        // 안전한 칸을 세기
        for (i in board.indices) {
            for (j in board[i].indices) {
                if (!dangerZone[i][j]) {
                    answer++
                }
            }
        }
        
        return answer
    }
}
