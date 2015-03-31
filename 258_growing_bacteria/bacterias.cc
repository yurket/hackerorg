#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


// count the n's member of arithmetic progression.
// !int overflow vulnerable!
static long long arithmetic_A(int a0, int n, int d)
{
    if (n == 0)
        return a0;
    return a0 + (n-1)*d;
}


static long long fib(int n)
{
    long long a0 = 2, a1 = 3;
    long long sum = 0;
    while (n--)
    {
        sum = a0+a1;
        a0 = a1;
        a1 = sum;
    }
    return a1;
}

static long long fib2(int n)
{
    long long a0 = 2, a1 = 4;
    long long sum = 0;
    while (n--)
    {
        sum = a0+a1;
        a0 = a1;
        a1 = sum;
    }
    return a1;
}

int main()
{
    auto i = 0;
    while (++i)
    {
        cout << "fib1= " << fib(i) << ", fib2=" << fib2(i) << std::endl << std::endl;
        if (fib(i)+fib2(i) > pow(10, 12))
        {
            
            cout << "number is " << i << std::endl;
            cout << "final answer is " << i+4 << std::endl;
            cout << "fib1= " << fib(i) << ", fib2=" << fib2(i) << std::endl << std::endl;
            break;
        }
    }
    return 0;
}

