#include<stdio.h>
int main()
{
 int num,i;
 i=1;
 scanf("%d",&num);
 num=num*2;
 for ( i = 1; i < num; i++)
 {
     i+=i;
 }
 printf("%d",i);
}