#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "TestTools.h"

#define MAX_CAKES 10

FILE *fr;

void printCakes(char *cakes);
char toggle(char in);
char *flipper(char *cakes, int offset, int width);
int flipTheCakes(char *cakes, int flipSize);
bool isFinished(char *cakes);

int main(int argc, char **argv) {

    //fr = fopen("cake_input.txt", "r");
    fr = fopen("A-small-practice.in", "r");
    if (fr) {
        printf("Begin testing.\n");
        printf("===================================\n");
        int numberOfTests = getNumberFromInput(fr);
        printf("Number of tests: %d\n", numberOfTests);
        for (int i = 0; i < numberOfTests; i++) {
            printf("Case #%3d:", i + 1);
            char *cakes = getTest(fr);
            int flipSize = getNumberFromInput(fr);
            int numberOfCakes = getNumberOfCakes(cakes);

            bool allDone = false;

            allDone = isFinished(cakes);
 
            int numberOfFlips = flipTheCakes(cakes, flipSize);
            allDone = isFinished(cakes);
            if (allDone)
                printf("%d\n", numberOfFlips);
            else
                printf("IMPOSSIBLE!\n");

        }
    }
    fclose(fr);
    return 0;
}

void printCakes(char *cakes) {
    printf("Current State of the Cakes: ");
    for (int i = 0; i < MAX_CAKES; i++)
        printf("%c", cakes[i]); 
    printf("\n");
}

char toggle(char in) {
    if (in == '+')
        return '-';
    else
        return '+';
}

char *flipper(char *cakes, int offset, int flipSize) {
    for (int i = offset; i < (offset + flipSize); i++)
        cakes[i] = toggle(cakes[i]);
}

int flipTheCakes(char *cakes, int flipSize) {
    int numberOfCakes = getNumberOfCakes(cakes);
    int numberOfFlips = 0;
    for (int i = 0; i < (numberOfCakes - flipSize + 1); i++)
        if (cakes[i] == '-') {
            flipper(cakes, i, flipSize);
            ++numberOfFlips;
        }
    return numberOfFlips;
}

bool isFinished(char *cakes) {
    int numberOfCakes = getNumberOfCakes(cakes);
    for (int i = 0; i < numberOfCakes; i++)
        if (cakes[i] == '-')
            return false;
    return true;
}
