#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(int age) {
    string answer = "";
    string alpha = "abcdefghij";
    while(age > 0){
        answer = alpha[age%10] + answer;
        age /= 10;
    }
    
    return answer;
}