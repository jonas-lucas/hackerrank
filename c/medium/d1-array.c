// 1D Arrays in C

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    int sum = 0;
    scanf("%d", &n);
    int ar[n];    

    for (int i = 0; i < n; i++) {
        scanf("%d", &ar[i]);
        sum = sum + ar[i];
    }

    printf("%d\n", sum);
    
    return 0;
}