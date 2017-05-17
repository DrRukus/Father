#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "TestTools.h"

#define MAX_CAKES 10

int getNumberFromInput(FILE *fr) {
    char c;
    char numberArray [5];
    int charCount = 0;
    while ((c = getc(fr)) != '\n') {
        numberArray[charCount++] = c;
    }   
    int multiple = charCount;
    int number = 0;
    for (int i = 0; i < charCount; i++) {
        int digit = numberArray[i] - '0';
        number += (pow(10, (multiple - 1)) * digit);
        --multiple;
    }   
    return number;
}

char *getTest(FILE *fr) {
    char *cakes = malloc(MAX_CAKES);
    //printf("So far so good!\n");
    char c;
    int cakeCount = 0;
    while ((c = getc(fr)) != ' ') {
        cakes[cakeCount++] = c;
    }   
    //fclose(fr); 
    return cakes;
}

int getFlipperSize(FILE *fr) {
    //int width = 0;
    char c;
    //int powerOfTen = 1;
    int digit;
    while (((c = getc(fr)) != '\n')) {// && powerOfTen >= 0) {
        digit = c - '0';
        //printf("%c -> %d, %d\n", c, digit, powerOfTen);
        //width += digit;
    }    
    return digit;
}

int getNumberOfCakes(char *cakes) {
    int cakeCount = 0;
    while (cakes[cakeCount] == '+' || cakes[cakeCount] == '-') {
        ++cakeCount;
    }
    return cakeCount;
}
