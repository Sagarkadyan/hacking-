
AIM
To write a C-program to convert a given number into binary number


ALGORITHM


STEP1:Start the program execution
STEP2:Read the decimal number
STEP3:Perform number mod 2 to find the reminder and save the reminder in sum.
STEP4:Divide the number by 10 to get the quotion
STEP5:Print the binary number in sum 
STEP6:Stop the program execution




PROGRAM






#include <stdio.h>
#include <stdlib.h>
// this program convert no into binary 

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




this program convert no into binary 


OUTPUT


Enter the decimal no:10
Equivalent binary nois 1010


RESULT




Thus the C-program had been wreitten ,executed sussesfully to perform decimal to binary conversion*/

