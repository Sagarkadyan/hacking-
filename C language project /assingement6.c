 #include<stdio.h>
 void  main()
 {
 int a,b,c,ch;
 printf("\n Enter the  values:");
 scanf("%d%d",&a,&b);
 printf("\n Enter the choice:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.division\n5.Modulo\nchoice:");
 scanf("%d",&ch);
 switch (ch)
 
 {
 case 1: printf("\n Addition of %d+%d is %d",a,b,a+b);
 break;
 case 2: printf("\n subtraction of %d-%d is %d",a,b,a-b);
 break;
 case 3: printf("\n Multiplicaion of %d*%d is %d ",a,b,a*b);
 break;
 case 4:if(b==0)
 printf("\nDiviion is not possiible");
 else
 printf("\n Division of %d/%d is %f",a,b,(float)a/b);
 break;
 case 5: printf("\n modulus  of %d%%%d is %d ",a,b,a%b);
 break;
 default: printf("\n Enter correct choice");
 break;
 }
 getchar();    
 }