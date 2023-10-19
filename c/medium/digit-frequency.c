// Digit Frequency

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    
    int lista[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = 0; i < strlen(s); i++) {
        if (isdigit(s[i])) {
            int digit = s[i] - '0';
            if (digit >= 0 && digit <= 9) {
                lista[digit]++;
            }
        }
    }
    
    for (int i = 0; i < 10; i++) {
        printf("%d ", lista[i]);
    }
    printf("\n");
    return 0;
}
