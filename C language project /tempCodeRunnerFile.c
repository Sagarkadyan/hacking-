#include<stdio.h>
void main()
{
int n,i,j;
printf("\nEnter the limit:");
scanf("%d",&n);
for (i=1;i <=n;i++)
{
for (j=2;j<i;j++)
{
if(i%j==0)    
break;
}   
if(i==j)
printf("%d",i); 
}    
getchar();
}