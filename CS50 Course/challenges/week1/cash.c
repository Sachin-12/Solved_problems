#include <cs50.h>
#include <math.h>
#include <stdio.h>
int main(void)
{
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;
    int pennies = 1;
    int coins_used = 0;
    do
    {
        float dollars = get_float("Change owed: ");
        int cents = round(dollars * 100);
        if (cents >= 1)
        {
            coins_used = cents / quarters;
            if (cents % quarters != 0)
            {
                cents = cents % quarters;
                if (cents % dimes != 0)
                {
                    coins_used = coins_used + (cents / dimes);
                    cents = cents % dimes;
                    if (cents % nickels != 0)
                    {
                        coins_used = coins_used + (cents / nickels);
                        cents = cents % nickels;
                        if (cents % pennies != 0)
                        {
                            coins_used = coins_used + (cents / pennies);
                        }
                        else{
                            coins_used = coins_used + (cents/pennies);
                        }
                    }
                    else
                    {
                        coins_used = coins_used + (cents / nickels);
                    }
                }
                else
                {
                    coins_used = coins_used + (cents / dimes);
                }
                printf("I have %i coin(s)\n", coins_used);
            }
            else
            {
                printf("I have %i coin(s)\n", coins_used);
            }
        }
        else
        {
            continue;
        }

    } while (true);
}
