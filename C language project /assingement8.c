#include <stdio.h>

long int factorial(long int);
int main()
{
long int no,fact;
//system("clear");
printf("\n enter a number...");
scanf("%ld",&no);
fact=factorial(no);
printf("\n the factorial of the given number id :%ld",fact);
getchar;    
}
long int factorial(long int n)
{
int i;
long int fact=1;
for(i = 1;i <= n; i++){
  fact=fact*i;
}
return fact;      
}