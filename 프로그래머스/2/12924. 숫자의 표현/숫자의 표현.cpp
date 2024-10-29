#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;    
    for(int i = 1; i <= n; i++){
        int sum = 0;
        for( int j = i; j <= n; j++){
            if( n - sum == j ){
                answer += 1;
                break;
            }else{
                if( sum > n){
                    break;
                }
                sum += j;
            }
        }
    }
    
    return answer;
}

// 1부터 더한다.
// n-sum < i크면 중지
// n == sum 같다면 answer += 1
