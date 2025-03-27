/*
AIM
To write a C program to design a simple menu-driven calculator
ALGORITHM
STEP1.Start the program execution
STEP2.Declare 2 variable a and b ,ch,c
STEP3.Get choice 1.addition,2.subtraction,3.multiplaction,4.dividion,5.modulation
STEP4.If ch=1,perform addition and print the result
STEP5.If ch=2,perform subtration and print the result.
STEP6.If ch=3,perform multiplaction and print the result.
STEP7.If ch=4,perform dividion and print the result.
STEP8.If ch=5,perform modulation and print the results
STEP9.If choice is not in them print"Enter correct choice"
STEP10.Stop thr program execution
PROGRAM*/
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

 /*
 