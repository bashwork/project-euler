#include <stdio.h>

int is_palindrome(int number, int base)
{
    int result = 0, copy = number;
    
    while (copy > 0) {
        result = (result*base) + (copy % base);
        copy  /= base;
    }
    return result == number;
}

int main(void)
{
    int result = 0, count = 1;
    
    for (count; count < 1000000; ++count) {
        if (   is_palindrome(count, 2)
            && is_palindrome(count, 10)) {
            result += count;
        }
    }
    printf("%d\n", result);
}

