#include <iostream>
#include <thread>

void threadFunction()
{
    std::cout << "Hi from thread!\n";
}

int main()
{
    std::thread th(&threadFunction);
    std::cout << "Hi from main!\n";
    th.join();
    return 0;
}
