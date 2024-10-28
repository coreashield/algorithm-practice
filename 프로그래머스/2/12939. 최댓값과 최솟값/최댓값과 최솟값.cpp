#include <iostream>
#include <string>
#include <sstream>
#include <climits>

using namespace std;

string solution(string s) {
    int min_value = INT_MAX;
    int max_value = INT_MIN;
    stringstream ss(s);
    int num;

    while (ss >> num) {
        min_value = min(min_value, num);
        max_value = max(max_value, num);
    }

    return to_string(min_value) + " " + to_string(max_value);
}
