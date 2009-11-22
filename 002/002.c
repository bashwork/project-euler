#include <stdio.h>

/* recursive */
long fibr(long a, long b)
{
    return (b > 4000000)
    ? 0
    : fibr(b, a + b) + ((b % 2 == 0) ? b : 0);
}

/* non recursive */
long fib(long a, long b)
{
    int c = 0 ,sum = 0;

    while (c < 4000000) {
        c = a + b;
        a = b;
        b = c;
        if (c % 2 == 0) sum += c;
    }
    return sum;
}

int main(void)
{
    printf("Result %ld\n", fibr(0, 1));
    printf("Result %ld\n", fib(0, 1));
    return 0;
}
