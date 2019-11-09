#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int main(void)
{
    do
    {
        int len = 0;
        int i = 0;
        unsigned long n = 1;
        int k = 0;
        int j = 0;
        unsigned long m = 0;
        unsigned long odd = 0;
        unsigned long even = 0;
        unsigned long numbers[16];
        unsigned long split_num = 0;
        char buffer[20];
        long credit_num = get_long("Number: ");
        sprintf(buffer, "%ld", credit_num);
        string s = buffer;
        len = strlen(s);
        if (len == 13)
        {
            for (i = len - 1; i >= 0; i--)
            {
                n = credit_num % 10;
                credit_num = credit_num / 10;
                numbers[i] = n;
            }
            for (i = 0; i < len; i = i + 2)
            {
                odd = numbers[i];
                if (odd != 0)
                {
                    odd = odd * 2;
                    if (odd > 9)
                    {
                        m = odd % 10;
                        m = m + odd / 10;
                        split_num = split_num + m;
                    }
                    else
                    {
                        split_num = split_num + odd;
                    }
                }
            }

            for (i = 1; i < len; i = i + 2)
            {
                even = numbers[i];
                split_num = split_num + even;
            }
//             printf("%lu\n", split_num);
            if (split_num % 10 == 0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("Invalid Card: \n");
            }
        }
        else if (len == 15)
        {
            for (i = len - 1; i >= 0; i--)
            {
                n = credit_num % 10;
                credit_num = credit_num / 10;
                numbers[i] = n;
            }
            for (i = 0; i < len; i = i + 2)
            {
                odd = numbers[i];
                if (odd != 0)
                {
                    odd = odd * 2;
                    if (odd > 9)
                    {
                        m = odd % 10;
                        m = m + odd / 10;
                        split_num = split_num + m;
                    }
                    else
                    {
                        split_num = split_num + odd;
                    }
                }
            }

            for (i = 1; i < len; i = i + 2)
            {
                even = numbers[i];
                split_num = split_num + even;
            }
//             printf("%lu\n", split_num);
            if (split_num % 10 == 0)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("Invalid Card: \n");
            }
        }
        else if (len == 16)
        {
            for (i = len - 1; i >= 0; i--)
            {
                n = credit_num % 10;
                credit_num = credit_num / 10;
                numbers[i] = n;
            }
            for (i = 0; i < len; i = i + 2)
            {
                odd = numbers[i];
                if (odd != 0)
                {
                    odd = odd * 2;
                    if (odd > 9)
                    {
                        m = odd % 10;
                        m = m + odd / 10;
                        split_num = split_num + m;
                    }
                    else
                    {
                        split_num = split_num + odd;
                    }
                }
            }

            for (i = 1; i < len; i = i + 2)
            {
                even = numbers[i];
                split_num = split_num + even;
            }
//             printf("%lu\n", split_num);
            if (split_num % 10 == 0)
            {
                printf("MASTER CRAD\n");
            }
            else
            {
                printf("Invalid Card: \n");
            }
        }
        else
        {
            printf("INVALID \n");
        }
    } while (true);
}
