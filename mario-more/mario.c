#include <cs50.h>
#include <stdio.h>
void mario_1(int Height);
int main(void)

{
    int Height;
    do
    {
        Height = get_int("Height: ");
    }
    while (Height <= 0);
    mario_1(Height);
}

void mario_1(int Height)
{
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
        printf("  ");
        for (int l = 1; l <= i; l++)
        {
            printf("#");
        }
        printf("\n");
    }
}
