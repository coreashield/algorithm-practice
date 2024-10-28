#include <string>
#include <vector>

using namespace std;

string solution(string n_str) {
    string answer = "";
    for(size_t i = 0; i < n_str.size(); i++){
        if( n_str[i] == '0' && answer == "" ){
            continue;
        }else{
            answer += n_str[i];
        }
    }
    return answer;
}