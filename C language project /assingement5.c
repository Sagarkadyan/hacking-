#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct student
{
int id;
char name[30];
float percentage;    /* data */
};
int main()

{
int i;
struct student record[3];
//ehich defined the three elements ,each of which is a type of 
//structstudents ,i.e each is an student structure.
// .1st  student's record
record[0].id=1;
strcpy(record[0].name,"raju");
record[0].percentage=86.5;
// 2nd student 's record
record[1].id=2;
strcpy(record[2].name,"surender");
record[1].percentage=90.5;
// 3rd student's record
record[2].id=3;
strcpy(record[2].name,"thiyagu");
record[2].percentage=81.5;
for(i=0;i<3;i++)
{
printf("\n Record of students : %d \n",i+1);
printf("\n Id is : %d \n ",record[i].id);
printf("\n Name i : %s \n",record[i].name);
printf("\n Percantage is : %f \n\n",record[i].percentage);;    
}

}