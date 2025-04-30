#include<stdio.h>
#include<stdlib.h>
void main()
{
   int c,pos;
   FILE *fpl;
   system("clear");
   fpl=fopen("sudent.txt","r+");//the file has something to write in it
   printf("\nReading from the file ...\n");
   while(!feof(fpl))
   {
       c=fgetc(fpl);
       printf("%c",c);

   } 
rewind(fpl);//position the pointer to the begging of the file 
c=fgetc(fpl);
printf("\nThe  first cgaracter from the file : % c",c);
pos=ftell(fpl);//return th ecurrent position of the file pointer
printf("\nThe position of the file pointer :%d",pos);
fseek(fpl,10,SEEK_SET);//Moves the files pointer to the 10th byte  from the beginning
pos=ftell(fpl);
c=fgetc(fpl);
printf("\nThe character at %d is %c  (from the beginning)",pos,c);
fseek(fpl,-5,SEEK_CUR);// moves the file pointer back to the 5th byte
//from the current position 
pos=ftell(fpl);
c=fgetc(fpl);
printf("\n The character at %d id : %c",pos,c);
fseek(fpl,12,SEEK_CUR);//moves the file pointer fordward to the 12 th
//byte from the current position 
pos=ftell(fpl);
c=fgetc(fpl);
printf("\nThe character at %d is :%c",pos,c);
getchar();
}