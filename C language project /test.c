#include <stdio.h>

int main() {
  int sachin[6];
  //input
  for (int i = 0; i < 6; i++)
  {
     printf("%d elemnts: ",i);
     scanf("%d",&sachin[i]);
   }
   // output
   for (int i = 0; i < 6; i++)
   {
      printf("%d element are : %d  \n",i,sachin[i]);
   }
   
  
   return 0;
}; 