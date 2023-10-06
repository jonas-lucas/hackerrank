// Sum of Digits of a Five Digit Number

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    
    int s = 0;
    
    while (n != 0) {
        s += n % 10;
        n /= 10;
    }
    
    printf("%d\n", s);
    
    return 0;
}