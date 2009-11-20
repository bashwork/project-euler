using System;
using System.Linq;

public class Problem001
{
    public static void Main()
    {
        var result = Enumerable.Range(0,1000)
            .Where(n => n % 3 == 0 or n % 5 == 0).Sum();
        Console.WriteLine("Result {0}", result);
    }
}
