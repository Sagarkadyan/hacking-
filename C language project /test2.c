#include <stdio.h>

// Function to return the maximum of two numbers
int main(int n1, int n2) {  // Function does not return a value (void)
    scanf("%d %d", &n1, &n2);
    if (n1 > n2)
        printf("%d", n1);
    else
        printf("%d", n2);
     return 0;
}
