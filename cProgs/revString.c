#include <stdio.h>

#define STRING_SIZE 8

void printString(char string[STRING_SIZE]);

int main(int argc, char *argv) {

    char string[STRING_SIZE] = {'a', 'b', 'c', 'd', 'e', 'g', 'h', 'i'};

    printString(string);

    char reversedString[STRING_SIZE];
    for (int i = 0; i < STRING_SIZE; i++) {
        reversedString[i] = string[STRING_SIZE - i - 1];
    }

    printString(reversedString);

    return 0;
}

void printString(char string[STRING_SIZE]) {
    for (int i = 0; i < STRING_SIZE; i++) {
        printf("%c", string[i]);
    }
    printf("\n");
}
