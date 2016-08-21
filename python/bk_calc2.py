#!/usr/bin/env python

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'
VERBOSE = True


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = None
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        self.pos = 0

        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        #index = 0
        left = 0
        right = 0
        if VERBOSE:
            print "Left side..."
        while str(self.current_token.value).isdigit():
            left = left * 10 + self.current_token.value
            if VERBOSE:
                #print "\nIndex:         {0}".format(index)
                print "Current Token: {0}".format(self.current_token.value)
                print "Left:          {0}".format(left)
                print "Right:         {0}".format(right)
            self.eat(INTEGER) 
            #index += 1
            
        # we expect the current token to be a single-digit integer
        #left = self.current_token
        #self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        if op.value == "+":
            self.eat(PLUS)
        elif op.value == "-":
            self.eat(MINUS)
        else:
            self.error()

        #index = 0
        if VERBOSE:
            print "Right side..."
        while str(self.current_token.value).isdigit():
            right = right * 10 + self.current_token.value
            if VERBOSE:
                #print "\nIndex:         {0}".format(index)
                print "Current Token: {0}".format(self.current_token.value)
                print "Left:          {0}".format(left)
                print "Right:         {0}".format(right)
            self.eat(INTEGER)
            #index += 1

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        if op.value == "+":
            result = left + right
        else:
            result = left - right
        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = raw_input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()