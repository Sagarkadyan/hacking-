/*
AIM
To write a C-program to print the Fibnacci series using functions.
ALGORITHM
STEP1.Start the program execution
STEP2.Read the Finbonacci range()
STEP3.Call function Fibonacci numbers
STEP4.Print the Fibonacci numbers
STEP5.Stop the program execution
PROGRAM*/
#include<stdio.h>
#include<stdlib.h>
void fib(int);
void main()
{
int n;
system("clear");
printf("\nEnter the limit:");
scanf("%d",&n);
fib(n);
getchar();
}
void fib(int n)
{
int i,a=0,b=1,c;
printf("\nFibnocci series are:");
printf("\n\n%d\t%d",a,b);
for ( i = 3; i < n; i++)
{
    c=a+b;
    a=b;
    b=c;
    printf("\t%d",c);
}
    
}
/*
OUPUT
Enter the the limit:5
Fibonacci series are 
0 1 1 3 5 */
