#include <stdio.h>
#include <stdlib.h>

int main()  
{
    float sa, da, fa;
    char operation;
    char input[50];  // Buffer to hold the input

    while (1) {   
        // Read the full line of input
        if (fgets(input, sizeof(input), stdin) == NULL) {
            break; // Exit if input fails
        }

        // Trim any trailing newline character
        if (input[0] == 'e' && (input[1] == '\n' || input[1] == '\0')) {
            break; // Exit if user enters 'e' alone
        }

        // Parse the operation and two numbers
        if (sscanf(input, " %c %f %f", &operation, &sa, &da) != 3) {
            continue; // Skip invalid inputs silently
        }

        // Perform the calculation based on the operation
        switch (operation) {
            case '+':
                fa = sa + da;
                printf("%f\n", fa);
                break;
            case '-':
                fa = sa - da;
                printf("%f\n", fa);
                break;
            case '*':
                fa = sa * da;
                printf("%f\n", fa);
                break;
            case '/':
                if (da != 0) {
                    fa = sa / da;
                    printf("%f\n", fa);
                } else {
                    printf("Error: Division by zero is not allowed.\n");
                }
                break;
            default:
                continue; // Ignore invalid operations
        }
    }

    return 0;
}
