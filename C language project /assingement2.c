

AIM : To write a C program to calculate the Simple and Compound intrest.



Algorithim


STEP1:start the program 
STEP2:declare the values p,n,ch,r
STEP3:input the values for p,n,r,ch
STEP4:get the choice from user weather to calcualte simple or compound intrest 
STEP5:claculate the print the value of simple intrest  or compound intrest 
STEP6:stop the program  


CODING


#include<stdio.h>
#include<math.h>
#include <stdlib.h>
// sometimes #ivclude<coinio.h> dont work in linux 
// sometimes clrscr does not work
//sometimes getch does not work
// so we use system("clear")and getchar
int main()
{
int p,n,ch;
float r;
system("clear");
printf("\n Enter the choice:\n1.Simple intrest \n2.Comound intrest: \nchoice: ");
scanf("%d",&ch);
printf("\nEnter the value of amount , number of years and rate of intrest:");
scanf("%d%d%f",&p,&n,&r);
switch(ch)
{
case 1: printf("\n The simple intrest is = %f", (p * n * r) / 100);
break;

case 2: printf("\n The compound intrest is = %f",(p * pow((1 +(r /100)),n)-p));
break;
default:printf("\nEnter the correct choice:");
break;
}
return 0;
}


OUTPUT 

Enter the choice:
  1. simple intrest
  2. compound intrest 
choice:1
Enter the value of amount ,number of years and Rate of interest:
100 2 2
The simple  intrest is =400

RESULT

Thus the C program has been written, executed succesfully to calculate the simple interest and compound*/
  
