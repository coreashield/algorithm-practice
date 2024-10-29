#include <string>
#include <vector>
#include <bitset>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = n+1;
    int n_one_cnt = 0;
    int answer_one_cnt = 0;
    while(1){
        bitset<8> n_b(n);
        bitset<8> answer_b(answer);
//         n을 이진수로 변환하고 1의 개수를 카운트
//         answer 를 이진수로 변환하고 1의 개수를 카운트
        n_one_cnt = n_b.count();
        answer_one_cnt = answer_b.count();

//        1의 개수가 같다면 answer을 return        
        if (n_one_cnt == answer_one_cnt){
            return answer;
        }
        answer += 1;
    }
}


