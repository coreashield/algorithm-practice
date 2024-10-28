#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string str1, string str2) {
    int check = str2.find(str1);
   
    if(check>=0){
        return 1;
    }else{
        return 0;
    }
}