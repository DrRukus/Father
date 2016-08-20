#include <iostream>
#include <math.h>
#include <string>
#include <vector>
//#include <sstream>
#include "Interpreter.h"
using namespace std;

enum tokenFields {TYPE, VALUE};

string INTEGER = "INTEGER";
string PLUS = "PLUS";
string MINUS = "MINUS";
string EOFT = "EOF";

// Return true if token is a digit character, false otherwise
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

Interpreter::Interpreter(string text) {//, int textLen) {
    textLen = text.size();
    text = text;
    pos = 0;
    currentChar = text[pos];
    cout << "Creating first token now..." << endl;
    currentToken = getNextToken();
}

Interpreter::~Interpreter() {};

void Interpreter::advance() {
    ++pos;
    if (pos > (textLen - 1)) { currentChar = 'E'; }
    else { currentChar = text[pos]; }
}

void Interpreter::skipWhitespace() {
    while ((currentChar != 'E') && (currentChar != ' ')) {
        advance();
    }
}

string Interpreter::integer() {
    string result;
    while ((currentChar != 'E') && isDigit(currentChar)) {
        result = result += currentChar;
        advance();
    }
    cout << "Result: " << result << endl;
    return result;
}

vector<string> Interpreter::getNextToken() {
    // Lexical analyzer - breaks input string apart into tokens
    vector<string> token(2);
    while (currentChar != 'E') {
        cout << "Analyzing token..." << endl;
        if (currentChar == ' ') {
            skipWhitespace();
            continue;
        }
        if (isDigit(currentChar)) {
            token[0] = "INTEGER";
            cout << "Integer = " << INTEGER << endl;
            token[1] = integer();
            cout << "Token Type: " << token[0] << endl;
            return token;
        }
        if (currentChar == '+') {
            advance();
            token[0] = "PLUS";
            token[1] = string(1, currentChar);
            return token;
        }
        if (currentChar == '-') {
            advance();
            token[0] = "MINUS";
            token[1] = string(1, currentChar);
            return token;
        }
        //if (currentChar == 'q') {
        //    cout << "Exiting..." << endl;   
        //}
        token[0] = "EOFT";
        token[1] = string(1, 'E');
        currentChar = 'E';
    }
    //token[0] = "EOFT";
    //token[1] = string(1, 'E');
    return token;
}

void Interpreter::eat(string tokenType) {
    if (currentToken[TYPE] == tokenType) {
        currentToken = getNextToken();
    } else { cout << "Unrecognized token..."; }
}

string Interpreter::term() {
    vector<string> token = currentToken;
    eat(INTEGER);
    return token[VALUE];
}

int Interpreter::expr() {
    // Parser/Interpreter

    int result = stoi(term());
    while (currentToken[TYPE] == PLUS || currentToken[TYPE] == MINUS) {
        vector<string> token = currentToken;
        cout << "Current token type: " << currentToken[TYPE] << endl;
        cout << "Current token value: " << currentToken[VALUE] << endl;
        if (token[TYPE] == PLUS) {
            eat(PLUS);
            result = result + stoi(term());
        } else if (token[TYPE] == MINUS) {
            eat(MINUS);
            result = result - stoi(term());
        }
    }
    return result;
}
