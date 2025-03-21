#include<stdio.h>
#include<math.h>
#include <stdlib.h>
// sometimes #ivclude<coinio.h> dont work in linux 
int main()
{
int p,n,ch;
float r;
system("clear");
printf("\n Enter the choice:\n1.Simple intrest \n2.Comound intrest: \nchoice: ");
scanf("%d",&ch);
printf("\nEnter the value of amount number of years and rate of intrest:");
scanf("%d%d%f",&p,&n,&r);
switch(ch)
{
case 1: printf("\n The simple intrest is = %f", (p * n * r) / 100);
break;

case 2: printf("\n The compound intrest is = %f",(p *pow((1 +(r /100)),n)-p));
break;
default:printf("\nEnter the correct choice:");
break;
}
return 0;
}
