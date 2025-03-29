/*
AIM
To write a C-program to swap two numbers using function by
(a) Pass by value
(b) Pass by reference
ALGORITHM
STEP1.Start the program execution
STEP2.Read a and b 
STEP3.Print a and b values before swaping
STEP4.Call function swap and pass 2 variable addresses 
STEP5.Function swap catches those addresses and swaps the addresses using a tempary varaible
STEP6.After swaping,print the values of a and b
STEP7.Stop the program execution
PROGRAM
*/
#include<stdio.h>
#include<stdlib.h>
void swap(int*,int*);

void main()
{
 int a,b;
 system("clear");
 printf("\nEnter two numbers:");
 scanf("%d%d",&a,&b);
 printf("\nCALL BY VALUE\n");
 printf("\nBefore swaping\n\n a=%d and b=%d",a,b);
 swap(&a,&b);
 printf("\nAfter swaping\n\n a=%d and b=%d",a,b);
 getchar();
 }
 void swap(int *a, int *b)
 {
 int t;
 t=*a;
 *a=*b;
 *b=t;

 }
 /*
 OUTPUT
 Enter two number : 10 20
 CALL BY VALUE 
 Before swaping
 a=10 and b=20
 After swaping 
 a=20 and b=1
 RESULT 
 Thus,the C-program had been written,executed successfully to swap
  two values using functions by call value  and call by reference
*/
