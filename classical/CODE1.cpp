#include <iostream>
#include <array>

std::array<int, 2> divComplex(std::array<int, 2> left, std::array<int, 2> right) {
    int divisor = right[0]*right[0] + right[1]*right[1];
    int a_top = left[0]*right[0] + left[1]*right[1];
    int b_top = left[1]*right[0] + left[0]*right[1];

    return std::array<int, 2>{a_top/divisor, b_top/divisor};
}


int main() {
    return 0;
}