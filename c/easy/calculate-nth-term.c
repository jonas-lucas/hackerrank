// Calculate the Nth term

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find_nth_term(int n, int a, int b, int c) {
    if (n == 1) {
        return a;
    } else if (n == 2) {
        return b;
    } else {
        int aux_a, aux_b, aux_c;
        for (int i = 3; i < n; i++) {
            aux_c = a + b + c;
            aux_b = c;
            aux_a = b;
            c = aux_c;
            b = aux_b;
            a = aux_a;
            printf("Step %d: %d %d %d\n", i, a, b, c);
        }
        return c;
    }
}


int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
