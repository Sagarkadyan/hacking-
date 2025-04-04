#include <stdio.h>

// Function to return the maximum of two numbers
void max(int n1, int n2) {  // Function does not return a value (void)
    if (n1 > n2)
        printf("%d", n1);
    else
        printf("%d", n2);
}

int main() {
    int n1, n2;
    scanf("%d%d", &n1, &n2);  // Read input

    max(n1, n2); // Call the function

    return 0;
}