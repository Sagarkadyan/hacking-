#include<stdio.h>
#include<stdlib.h>
void main()
{
int ch ,b,h,a,c;
float r;
system("clear");
printf(" Enter the choice:\n1.circle\n2.square\n3.rectangle\n4.triangle\nchoice:");
scanf("%d",&ch);
switch (ch)
{
case 1: printf("\nenter the radius of the circle:");/* constant-expression */
   scanf("%f",&r);
   printf("\narea of circle=%f",3.14 * r * r);
   printf("\nperimeter of circle=%f",2*3.14 * r);
    /* code */
   break;
case 2: printf("\nEnter the side of the square:");
    scanf("%d",&a);
    printf("\nArea of the square id %d",a*a);
    printf("\nPerimeter of square=%d",4*a);

    break;
case 3: printf("\nEnter the breadth and height of rectangle:");
   scanf("%d%d",&b,&h);
   printf("\nArea of the rectangle:%d",b*h);
   printf("nPerimeter of the rectangle:%d",2*(b+h));
   break; 
case 4:printf("\nEnter the breadth and height of triandle :");
     scanf("%d%d",&b,&h);
     printf("\nEnter the three ide of triangle:");
     scanf("%d%d%d",&a,&b,&c);
     printf("\nArea of triangle:%f",(float)(0.5*b*h));
     printf("\nPerimeter of triangle:%f",(float)(a+b+c));
     break;
default:printf("\nEnter the correct choice:");
break;
}    
getchar;
}