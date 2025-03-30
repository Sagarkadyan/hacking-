#include<stdio.h>
#include<string.h>
int main()
{
    
    char str[100];
    char ch;
    int count = 0;

        while (1) {
        scanf("%c", &ch);
        if (ch == '$') break;  
        if (ch != ' ') count++; 
    }

    printf("%d\n", count);
    return 0;
}   