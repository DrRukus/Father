#ifndef TESTTOOLS_H
#define TESTTOOLS_H

int getNumberFromInput(FILE *fr);
char *getTest(FILE *fr);
int getFlipperSize(FILE *fr);
int getNumberOfCakes(char *cakes);
char *getInputLine(FILE *fr);
int convertToInt(char numArray[], int numberOfDigits);
int getNumberOfChars(int num);
char *convertToChars(int num);

#endif
