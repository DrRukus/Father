#ifndef TOKEN_H
#define TOKEN_H

class Token {
public:
    const char* type;
    char value;
    Token(const char* type, char value);
};
#endif
