class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        // MutableList로 플레이어 목록을 유지
        val playerList = players.toMutableList()
        
        // 선수 이름과 인덱스를 매핑하는 해시맵 생성
        val playerIndexMap = mutableMapOf<String, Int>()
        for (i in players.indices) {
            playerIndexMap[players[i]] = i
        }

        // callings 배열을 순회
        for (i in callings) {
            // 현재 선수의 인덱스를 맵에서 가져옴
            val index = playerIndexMap[i] ?: continue
            
            // 만약 인덱스가 첫 번째가 아니면 위치를 교환
            if (index > 0) {
                // 앞의 선수와 현재 선수의 위치를 교환
                val previousPlayer = playerList[index - 1]
                playerList[index - 1] = i
                playerList[index] = previousPlayer
                
                // 맵에서 인덱스 업데이트
                playerIndexMap[i] = index - 1
                playerIndexMap[previousPlayer] = index
            }
        }

        // 최종 배열 반환
        return playerList.toTypedArray()
    }
}
