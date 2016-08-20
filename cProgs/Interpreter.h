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

class Interpreter {
private:
    int textLen;
    std::string text;
    int pos;
    std::vector<std::string> currentToken;
    char currentChar;

    void advance();
    void skipWhitespace();
    std::string integer();
    std::vector<std::string> getNextToken();
    void eat(std::string);
    std::string term();

public:
    Interpreter(std::string);
    ~Interpreter();
    int expr();

};
#endif
