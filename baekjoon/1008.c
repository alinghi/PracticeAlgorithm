#include <stdio.h>

int main(void) {

    int a=0;
    int b=0;
    double c=0;
    double d=0;
    scanf("%d %d", &a, &b);
    c=(double)a;
    d=(double)b;
    d=c/d;
    printf("%0.15f\n", d);
    return 0;
}