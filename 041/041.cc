#include <iostream>
#include <vector>
#include <algorithm>

bool is_prime(int n)
{
    for (int i = 2; i*i < n; i++) {
        if (!(n%i)) return false;
    }
    return true;
}

int sum(std::vector<int> input)
{
    int result = 0;
    std::vector<int>::iterator start, end = input.end();

    for (start = input.begin(); start != end; ++start) {
        result = (*start) + result * 10;
    }

    return result;
}

int main(void)
{
    int result = -1;
    std::vector<int> set;

    for (int i = 7; i > 0; --i) {
        set.push_back(i);
    }

    while (std::prev_permutation(set.begin(), set.end())) {
        result = sum(set);
        if (is_prime(result)) break;
    }

    std::cout << result << "\n";
    return 0;
}
