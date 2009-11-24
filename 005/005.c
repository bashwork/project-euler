#include <stdio.h>

long long int gcd(long long int a, long long int b)
{
    long long int c;

    while (b) {
        c = b;
        b = a % b;
        a = c;
    }

    return a;
}

long long int lcm(long long int a, long long int b)
{
    return (a * b) / gcd(a, b);
}

long long int get_solution()
{
    long long int i, s = 1;

    for (i = 2; i < 21; ++i) {
        s = lcm(s, i);
    }
    return s;
}

int main(void)
{
    printf("Result %lld\n", get_solution());
    return 0;
}
