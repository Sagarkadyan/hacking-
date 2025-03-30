#include <stdio.h>

int main() {
 int num,i;
 i=1;
 scanf("%d",&num);
 for ( i = 1; i <= num; i++)
 {if (i%3==0)
 {
    continue;
 } 
 if (i%7==0)
 {
    continue;
 }
   printf("%d\n",i);
 }
 
   return 0 ;
}/*
1
2
4
5
8
10
11
13
16
17
19
20
22*/