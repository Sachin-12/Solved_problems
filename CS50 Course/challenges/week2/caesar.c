#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
    int key_len = strlen(argv[1]);
    int i = 0;
    int j = 0;
    int k = 0;
    int b;
    int c = 0;
    int d = 0;
    int plain_txt_len;
    int isdigit = 0;
    char a[100];
    //     check if the no. of arguments is 2
    if (argc == 2)
    {
        //         check if the key is a valid number
        while (j < key_len && isdigit == 0)
        {
            if (argv[1][j] >= 48 && argv[1][j] <= 57)
            {
                isdigit = 0;
            }
            else
            {
                isdigit = 1;
            }
            j++;
        }
        //         if the key is valid proceed
        if (isdigit == 0)
        {
            printf("Success\n");
            k = atoi(argv[1]);
            //             get the plain text

            string plaintext = get_string("plaintext :");
            plain_txt_len = strlen(plaintext);
            for (i = 0; i < plain_txt_len; i++)
            {

                b = (int)plaintext[i];
                //                 check if the nth character is lowercase
                if (islower(plaintext[i]))
                {
                    for (c = 0; c < k; c++)
                    {
                        if (b == 122)
                        {
                            b = b - 25;
                        }
                        else
                        {
                            b++;
                        }
                    }
                    c = 0;
                    a[i] = b;
                }
                //                 check if the nth character is uppercase
                else if (isupper(plaintext[i]))
                {
                    for (c = 0; c < k; c++)
                    {
                        if (b == 90)
                        {
                            b = b - 25;
                        }
                        else
                        {
                            b++;
                        }
                    }
                    c = 0;
                    a[i] = b;
                }
                else
                {
                    a[i] = plaintext[i];
                }
            }
            printf("\nciphertext :");
            //             print cipher text
            for (d = 0; d < plain_txt_len; d++)
            {
                printf("%c", a[d]);
            }
            printf("\n");
            return 0;
        }
        else
        {
            printf("Usage ./caesar key");
            return 1;
        }
    }
    else
    {
        printf("Usage ./caesar key");
        return 1;
    }
}