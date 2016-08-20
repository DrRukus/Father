#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "Interpreter.h"
using namespace std;

int main(int argc, char* argv[]) {

    string text;

    while (1) {
        cout << "calc>";
        //text = (char *)malloc(nBytes + 1);
        //text = new char* [nBytes + 1]
        getline(cin, text);
        cout << text << std::endl;
        //break;

        Interpreter interpreter = Interpreter(text);//, numOfTokens);
        int result = interpreter.expr();
        cout << result << endl;
    }

    return 0;
}


