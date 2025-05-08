/*#include<stdio.h>
int main(){
    FILE *file;
    //Creating a file
    file = fopen("/home/sagar/Documents/hacking-/C language project /","w");
    // Cheacking wheather file is created or not 
    if (file ==NULL){
        printf("Error in creating file");
        return 1;
    }
    printf("File created.");
    return 0;

}
*/


#include<stdio.h>


 int main(){
     FILE * file;
     // opening the file 

    file =fopen("/home/sagar/Documents/hacking-/C language project /student.txt","w");
    // checking wheather  file is opened or not 
    if (file ==NULL){

        printf("\nError in opening file ");
        return 1;
    }
    printf("File opened");
    // closing the file 
    fclose(file);
    printf("\nFile closed");
    return 0; 
 }  



/*
#include<stdio.h>
struct employee
{
    int age ;
    float percent ;
    char *name;
};
int main(){
    FILE *fp ;
    struct employee emp[]={
        {25,65.5,"Ravi"},
        {21,75.5,"Roshan"},
        {24,60.5,"Reena"}
    };
    char *string ;
    fp = fopen("/home/sagar/Documents/hacking-/C language project /student.txt","w");
    for (int i= 0; i < 3; i++){
        fprintf(fp,"%d %f %s\n",emp[i].age,emp[i].percent,emp[i].name);

    }
    fclose(fp);
}











#include<stdio.h>
int main(){
    FILE *fp;
    // printing in file
    char *sub[]={"C programing Tutorial\n","c++ Tutorial\n","Python Tutorial\n"};
    fp=fopen("/home/sagar/Documents/hacking-/C language project /student.txt","w");
    for (int i = 0; i < 4; i++){
        fputs(sub[i],fp);

    }
    fclose(fp);
    return 0;
}