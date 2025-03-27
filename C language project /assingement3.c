/*
AIM:To write a C program to find the area and peremeter of circle,triangle,rectangle and square
PROCEDURE
STEP1:Start the program execution 
STEP2:Declare the variable ch,a,b,c,h,r
STEP3:Get the choice weather the  1.circle  2.square 3.rectangle 4.triangle
STEP4:If ch=1 read r and compute area  and perimeter of circle 
STEP5:Print the area and the perimeter of circle
STEP6:If ch=2 read a and copmute area perimeter of square
STEP7:Print the  area and perimeter of square
STEP8:If ch=3 read b,h and compute area and perimeter of reactangle 
STEP9:Print the area and the perimeter of rectangle
STEP10:If ch=4 read a,b,c and compute area  and perimeter of triangle
STEP11:Print the area and perimeter of triangle
STEP12:Stop the program execution
CODING
*/
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
/*OUTPUT
Enter the  choice :
  1.Circle
  2.Square
  3.Rectangle
  4.Triangle
Chice 1
Enter the radius of the circle:2
Area of ciccle=12.56
Perimeter of circle=12.56
*/ 