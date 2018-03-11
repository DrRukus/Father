#include <iostream>
#include <string>
#include <thread>
#include <future>

void thFun(std::promise<std::string> && prms)
{
    std::string str("Hello from future!");
    prms.set_value(str);
}

int main()
{
    std::promise<std::string> prms;
    std::future<std::string> ftr = prms.get_future();
    std::thread th(&thFun, std::move(prms));
    std::cout << "Hello from main!\n";
    std::string str = ftr.get();
    std::cout << str << std::endl;
    th.join();
}
