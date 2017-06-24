#include <stdio.h>

/* define your function here (don't forget to declare it) */
unsigned int factorial(unsigned int n) {
    if(n==1 || n == 0) {
    	return 1;
    }

    return n * factorial(n-1);
}

int main() {
    /* testing code */
    printf("1! = %i\n", factorial(1));
    printf("3! = %i\n", factorial(3));
    printf("5! = %i\n", factorial(5));
}
