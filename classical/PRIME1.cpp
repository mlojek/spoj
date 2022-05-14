#include <iostream>


bool isPrime(int number) {
    if (number < 2) {
        return false;
    }
    else if (number == 2) {
        return true;
    }
    else {
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
    }

    return true;
}


int main() {
    int loops;
    int start, stop;

    std::cin >> loops;

    for (int i = 0; i < loops; i++) {
        std::cin >> start >> stop;

        for (int j = start; j <= stop; j++)
            if (isPrime(j))
                std::cout << j << std::endl;

        std::cout << std::endl;
    }

    return 0;
}