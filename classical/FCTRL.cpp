#include <iostream>


int trailingZeros(int n) {
    int i = 2, sumi = 0;
    int j = 5, sumj = 0;

    while (i <= n) {
        sumi += n / i;
        i *= 2;
    }

    while (j <= n) {
        sumj += n / j;
        j *= 5;
    }

    if (sumi < sumj) return sumi; else return sumj; 
}


int main() {
    int loops, n;

    std::cin >> loops;

    for (int i = 0; i < loops; i++) {
        std::cin >> n;
        std::cout << trailingZeros(n) << std::endl;
    }

    return 0;
}