#include <iostream>
#include "add.h"

int main()
{
    std::cout << "Hello, World!" << std::endl;
    std::cout << "1 + 3 = " << add(1, 3) << std::endl;
    std::cout << "5 - 2 = " << sub(5, 2) << std::endl;
    return 0;
}