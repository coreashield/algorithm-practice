#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    for( int i = 2; i <= n; i++ ){
        if( n % i == 0){
            answer += 1;
        }
    }
    return answer;
}