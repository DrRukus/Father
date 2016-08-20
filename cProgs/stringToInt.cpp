#include <iostream>
#include <string>
#include <typeinfo>
#include <stdlib.h>
using namespace std;

int main(int argc, char* argv[]) {

    string str1 = "124";
    string str2 = "357";

    cout << typeid(0).name() << endl;
    cout << typeid(str1[0]).name() << endl;
    cout << typeid(str1[0] - '0').name() << endl;

    return 0;

}
