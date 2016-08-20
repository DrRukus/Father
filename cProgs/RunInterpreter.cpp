#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "Interpreter.h"
using namespace std;

int main(int argc, char* argv[]) {

    string text;

    while (1) {
        cout << "calc>";
        getline(cin, text);
        //cout << "Expression: " << text << std::endl;

        Interpreter interpreter = Interpreter(text);
        //cout << "Interpreter object created.  Calculating expression..." << endl;
        int result = interpreter.expr();
        cout << result << endl;
    }

    return 0;
}


