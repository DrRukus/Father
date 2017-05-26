#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "TestTools.h"

#define MAX_ARRAY 15

int main(int argc, char **argv) {

    char input[] = {'5', '4', '3'};
    int value = convertToInt(input, sizeof(input));

    int iterValue;
    for (iterValue = value; iterValue > 0; iterValue--) {
        int foundOne = 1;
        char *tempArr = convertToChars(iterValue);
        for (int j = 0; j < (getNumberOfChars(iterValue) - 1); j++)
            if ((tempArr[j] - '0') > (tempArr[j + 1] - '0')) {
                foundOne = 0;
                break;
            }
        if (foundOne)
            break;
    }

    printf("%d\n", iterValue);

    return 0;
}

