#include <stdio.h>

void printSize(char *testArr);

int main (int argc, char *argv) {
    
    char testArr [15] = {'a', 'a', 'a', 'a', 'a',
                         'a', 'a', 'a', 'a', 'a',
                         'a', 'a', 'a', 'a', 'a'};

    int size = sizeof(testArr);
    printf("%d\n", size);
    //printSize(testArr);

    return 0;
}

void printSize(char *testArr) {
    int size = sizeof(testArr);

    int i;
    for (i = 0; i < size + 7; i++) {
        printf("%c\n", testArr[i]);
    }

    printf("%d\n", i);

    printf("Size of array: %d\n", size);

}
