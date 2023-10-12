// Printing Pattern Using Loops

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);

    for (int i = n; i > 0; i--) {
        for (int j = n; j > 0; j--) {
            if (j > i) {
                printf("%d ", j);
            } else {
                printf("%d ", i);
            }
        }
        for (int j = 2; j < n + 1; j++) {
            if (j > i) {
                printf("%d ", j);
            } else {
                printf("%d ", i);
            }
        }
        printf("\n");
    }
    for (int i = 2; i < n + 1; i++) {
        for (int j = n; j > 0; j--) {
            if (j > i) {
                printf("%d ", j);
            } else {
                printf("%d ", i);
            }
        }
        for (int j = 2; j < n + 1; j++) {
            if (j > i) {
                printf("%d ", j);
            } else {
                printf("%d ", i);
            }
        }
        printf("\n");
    }
      
    return 0;
}
