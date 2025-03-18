#include <stdio.h>
#include <stdlib.h>

void main()
{
long int n,i=1,sum=0,r;
system("clear");
printf("\nEnter the decimal number:");
scanf("%ld",&n);
while(n>0)
{
r=n%2;
sum=sum+(r*i);
i=i*10;
n=n/2;    
}   
printf("\n Equivalent binary number is %ld",sum);
getchar();
}