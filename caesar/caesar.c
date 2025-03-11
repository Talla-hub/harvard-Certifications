#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
char rotate(char c, int n);
bool only_digits(string s);

int main(int argc, string argv[])
{
    // Ensure the program is run with exactly one numeric command-line argument
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1; // Exit with error code 1
    }

    // Convert the key to an integer
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    string text = get_string("plaintext: ");

    // Print ciphertext
    printf("ciphertext: ");
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        printf("%c", rotate(text[i], key));
    }
    printf("\n");

    return 0; // Exit successfully
}

// Function to rotate a character by n positions
char rotate(char c, int n)
{
    if (isupper(c))
    {
        return 'A' + (c - 'A' + n) % 26;
    }
    else if (islower(c))
    {
        return 'a' + (c - 'a' + n) % 26;
    }
    return c; // Non-alphabetic characters remain unchanged
}

// Function to check if a string contains only digits
bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}
