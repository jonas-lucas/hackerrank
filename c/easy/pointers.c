#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    int a1 = *a + *b;
    int b1 = abs(*a - *b);
    *a = a1;
    *b = b1;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d\n", a, b);

    return 0;
}
