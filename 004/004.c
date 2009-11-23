#include <stdio.h>
#include <string.h>

int is_palindrome(long int input)
{
    char a[10] = {'\0'};
    int i, j, r = 1;

    for (i = 0, j = input; j > 0; j /= 10)
        a[i++] = (j % 10) + '0';

    for (i = strlen(a) - 1; i > 0;)
        r &= a[i--] == a[j++];
    
    return r;
}

long int find_largest()
{
    long int a,b,t,m = 0;

    for (a = 999; a > 100; --a) {
        for (b = a; b > 100; --b) {
            t = a * b;
            if (is_palindrome(t) && t > m)
                m = t;
        }
    }

    return m;
}

int main(void)
{
    printf("Result %ld\n", find_largest());
    return 0;
}
