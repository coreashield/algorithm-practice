#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string num_str) {
    int answer = 0;
    for( size_t i = 0; i < num_str.size(); i++ ){
        int a = num_str[i] - '0';
        // cout << a << endl;
        answer += a;
    }
    return answer;
}