#include<stdio.h>
int main()
{
int arr[10],i,n,sum=0;
printf("\n enter the number of elements in the arry ");
// reading the size of the array
scanf("%d",&n);
printf("\n enter the values for the element of the array ");
for(i=0;i<n;i++)
{
   printf("\n enter the element %d ",i+1);
   scanf("%d",&arr[i]); 
}
for (i=0;i<n;i++)
{
    sum=sum+arr[i];
}
printf("\n printing the array elements .....");
printf("\n the values for the elements of the array");
for (i=0;i<n;i++)
{
    printf("\n the elements %d :%d",i+1,arr[i]);
}
printf("\n printing the  sum of array ...");
printf("%d",sum);  
}