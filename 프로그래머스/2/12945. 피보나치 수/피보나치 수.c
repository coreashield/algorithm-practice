#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    const int MOD = 1234567; // 나누어줄 값
    long long fib[n + 1]; // 피보나치 수를 저장할 배열
    fib[0] = 0; // F(0)
    fib[1] = 1; // F(1)

    // 2부터 n까지 피보나치 수 계산
    for (int i = 2; i <= n; i++) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD; // 나머지를 취함
    }

    return fib[n]; // n번째 피보나치 수 반환
}
