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

char *getInputLine(FILE *fr) {
    int length = 0;
    char *inputArr = malloc(18);
    char c;
    while ((c = getc(fr)) != '\n') {
        inputArr[length++] = c;
    }
    char *inputLine = malloc(length);
    for (int i = 0; i < length; i++) {
        inputLine[i] = inputArr[i];
    }
    return inputArr;
}

int convertToInt(char numArray[], int numberOfDigits) {
    int multiplier = numberOfDigits;
    int result = 0;
    for (int i = 0; i < numberOfDigits; i++) {
        int digit = numArray[i] - '0';
        result += (pow(10, ((multiplier--) - 1)) * digit);
    }
    return result;
}

int getNumberOfChars(int num) {
    return snprintf(NULL, 0, "%d", num);
}

char *convertToChars(int num) {
    char *resultArr = malloc(getNumberOfChars(num));
    sprintf(resultArr, "%d", num);
    return resultArr;
}
