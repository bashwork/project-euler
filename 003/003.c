#include <stdio.h>

long long unsigned gcd(long long unsigned input)
{
    long long unsigned  i;

    for (i = 2; i < input; ++i)
    {
        while (input % i == 0)
            input /= i;
        if (input == 1) break;
    }
    return i;
}

int main(void)
{
    printf("Result %llu\n", gcd(600851475143LLU));
    return 0;
}
