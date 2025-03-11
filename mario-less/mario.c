#include <cs50.h>
#include <stdio.h>
int main(void)
{
    int Height;
    do
    {
        Height = get_int("Height: ");
    }
    while (Height <= 0);

    for (int i = 1; i <= Height; i++)
    {
        for (int j = Height - i; j > 0; j--)
        {
            printf(" ");
        }
        for (int k = 1; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
