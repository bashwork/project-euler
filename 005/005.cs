using System;
using System.Linq;

public class Solution005
{
    static int gcd(int a, int b)
    {
        while (b != 0) {
            int c = b;
            b = a % b;
            a = c;
        }
        return a;
    }

    static int lcm(int a, int b)
    {
        return a * b / gcd(a, b);
    }

    static void Main()
    {
        var result = Enumerable.Range(1,20)
            .Aggregate((a,b) => lcm(a,b));
        Console.WriteLine("Result {0}\n", result);
    }
}
