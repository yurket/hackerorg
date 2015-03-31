#include <iostream>
#include <stdio.h>
#include <gmp.h>


static void fib(mpz_t result, int n)
{
    mpz_t a0, a1, sum;
    mpz_init(a0);
    mpz_init2(a1, 1);
    mpz_init(sum);
    while (n--)
    {
        mpz_add(sum, a0, a1);
        mpz_set(a0, a1);
        mpz_set(a1, sum);
        mpz_set(result, a1);
    }
    mpz_clear(a0);
    mpz_clear(a1);
    mpz_clear(sum);
}


int main()
{
    /* printf("answer is %d\n", fib(1500000)); */
    mpz_t fib_num;
    mpz_init(fib_num);
    mpz_fib_ui(fib_num, 150000000);
    /* gmp_printf("answer is %Zd\n", fib_num); */


    char *fib_buf = mpz_get_str(NULL, 10, fib_num);
    std::string fib_str(fib_buf);
    // std::cout << fib_str << std::endl;
    for (int i = 0; i < fib_str.length(); i++)
    {
        if (i % 20000 == 0)
        {
            std::cout << fib_str[i];
        }
    }
    return 0;
}

