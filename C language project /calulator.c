/*Write a program that acts as a calculator as in the previous lessons, but now it will get input from the user until he enters e.

Each input from the user will be separated by a new line (\n).

The calculation will be in the format operation float float (separated by space), where the possible operations are +,-,*,/.

Each output (calculation result) should also be separated by a new line.

Check the test cases for examples.*/
#include<stdio.h>

int main()  
{
    float sa,da,fa;
    char op;

  while  (1){   
    scanf("%c%f%f",&op,&sa,&da);
  
     if (op=='e')
     {
       break;
     }
     
     else if(op =='+'){
      fa=sa+da;
      printf("\n%f",fa);
    }
    else if (op =='-')
    {
        fa=sa-da;
        printf("\n%f",fa);
    }
    else if (op=='*')
    {
        fa=sa*da;
        printf("\n%f",fa);

    }
    else if(op=='/')
    {
     fa=sa / da;
     printf("\n%f",fa);    
    }
    else
    {
      break;
    }
    
  }
}
