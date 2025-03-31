#include<stdio.h>
#include<stdlib.h>


struct stu
{
    char name[100];
    int maths,phy,chem,rank;
    float cutoff;
};
void main()
{
 struct stu s[100],temp;
 int i,j,n;
 system("clear");
 printf("\n\n No. of Students.....");
 scanf("%d",&n);
 for ( i = 0; i < n; i++)
 {
    fflush(stdin);

    printf("\n Maths Mark...")
    scanf("%d", &s[i]..maths);

    printf("\nPhysics Marks...")
    scanf("%d",&s[i].phy);

    printf("\n Chemistry Mark......");
    scanf("%d", &s[i].chem);
       s[i].cutoff =(s[i].maths/2.0)+(s[i].phy/4.0)+(s[i].chem/4.0);


 }
// sort decending - cutoff
for ( i = 0; i < n; i++)
{
    for ( j = i+1; j < n; j++)
    {
       if (s[i].cuttoff < s[j].cutoff)
       {
           temp=s[i];
           s[i]=s[j];
           s[j]=temp;
       }
        
    }
        
}
 
    
}
