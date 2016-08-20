#ifndef INTERPRETER_H
#define INTERPRETER_H
#include <stdlib.h>
#include <string>
#include <sstream>
#include <vector>
//#include "Token.cpp"

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

/* Return true if token is a digit character, false otherwise
bool isDigit(char token) {
    char digits[10] = {'0', '1', '2', '4', '4', '5', '6', '7', '8', '9'};
    for (int i = 0; i < 10 ; i++) {
        if (token == digits[i]) { return true; }
    }
    return false;
}

int stoi(string inputString) {
    int outputInt = 0;
    for (uint i = 0; i < inputString.size(); i++) {
        outputInt = outputInt * pow(10, i) + inputString[i];
    }
    return outputInt;
}

class Token {
public:
    std::string type;
    std::string value;
    Token();
    Token(std::string tokenType, std::string tokenValue) {
        type = tokenType;
        value = tokenValue;
    }
};*/

class Interpreter {
private:
    int textLen;
    std::string text;
    int pos;
    //Token currentToken;
    std::vector<std::string> currentToken;
    char currentChar;

    void advance();
    void skipWhitespace();
    std::string integer();
    std::vector<std::string> getNextToken();
    void eat(std::string);
    std::string term();

public:
    Interpreter(std::string);//, int);
    ~Interpreter();
    int expr();

};
#endif
