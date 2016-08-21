#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include "Interpreter.h"
using namespace std;

int main(int argc, char* argv[]) {

    string text;

    while (1) {
        cout << "calc>";
        getline(cin, text);
        if (text.compare("q") == 0) { return 0; }

        Interpreter interpreter = Interpreter(text);
        int result = interpreter.expr();
        cout << result << endl;
    }

    return 0;
}


