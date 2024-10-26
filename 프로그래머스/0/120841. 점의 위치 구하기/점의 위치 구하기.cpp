#include <string>
#include <vector>
#include <iostream> // cout을 사용하기 위해 추가

using namespace std;

int solution(vector<int> dot) {
    int answer = 0;
    if( dot[0] < 0 && dot[1] < 0 ){
        return 3;
    }else if ( dot[0] < 0 && dot[1] > 0){
        return 2;
    }else if ( dot[0] > 0 && dot[1] > 0 ){
        return 1;
    }else{
        return 4;
    }
    

    return answer;
}