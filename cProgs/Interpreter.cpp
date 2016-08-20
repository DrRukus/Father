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
    char digits[10] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    for (int i = 0; i < 10 ; i++) {
        if (token == digits[i]) { 
            //cout << "Digit Detected!!!!!" << endl;
            return true; 
        }
    }
    //cout << "No digit detected???" << endl;
    return false;
}

int stoi(string inputString) {
    int outputInt = 0;
    for (uint i = 0; i < inputString.size(); i++) {
        outputInt = outputInt * pow(10, i) + (inputString[i] - '0');
    }
    return outputInt;
}

Interpreter::Interpreter(string inputText) {//, int textLen) {
    textLen = inputText.size();
    //cout << "Size: " << textLen << endl;
    text = inputText;
    pos = 0;
    currentChar = text[pos];
    //cout << "Creating first token now..." << endl;
    vector<string> currentToken(2);
}

Interpreter::~Interpreter() {};

void Interpreter::advance() {
    ++pos;
    if (pos > (textLen - 1)) { 
        currentChar = 'E';
    } else {
        //cout << "Current char before(advance function): " << currentChar << endl;
        currentChar = text[pos]; 
        //cout << "Current char after(advance function): " << currentChar << endl;
    }
    //cout << "Current char(advance function): " << currentChar << endl;
}

void Interpreter::skipWhitespace() {
    while ((currentChar != 'E') && (currentChar != ' ')) {
        advance();
    }
}

string Interpreter::integer() {
    string result;
    while ((currentChar != 'E') && isDigit(currentChar)) {
        //cout << "Result(int function): " << result << endl;
        result = result += currentChar;
        advance();
    }
    //cout << "Result(int function): " << result << endl;
    return result;
}

vector<string> Interpreter::getNextToken() {
    // Lexical analyzer - breaks input string apart into tokens
    vector<string> token(2);
    while (currentChar != 'E') {
        //cout << "Analyzing token..." << endl;
        //cout << "Current Char: " << currentChar << endl;
        if (currentChar == ' ') {
            skipWhitespace();
            continue;
        }
        if (isDigit(currentChar)) {
            token[0] = "INTEGER";
            //cout << "Integer = " << INTEGER << endl;
            token[1] = integer();
            //cout << "Token Type: " << token[0] << endl;
            return token;
        }
        if (currentChar == '+') {
            advance();
            //cout << "Current char: " << currentChar << endl; 
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
    currentToken = getNextToken();

    int result = stoi(term());
    //cout << "First term: " << result << endl;
    //cout << "Current token type(outside): " << currentToken[TYPE] << endl;
    //cout << "Current token value(outside): " << currentToken[VALUE] << endl;
    while (currentToken[TYPE] == PLUS || currentToken[TYPE] == MINUS) {
        vector<string> token = currentToken;
        //cout << "Current token type: " << currentToken[TYPE] << endl;
        //cout << "Current token value: " << currentToken[VALUE] << endl;
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
