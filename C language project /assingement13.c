#include<stdio.h>
//Bubble sort implementation 
void bubbleSort(int arr[],int n){
   for (int i = 0; i < n-1; i++){
     for(int j=0;j < n-i-1;j++){
       if(arr[j]>arr[j+1]){
         int temp =arr[j];
         arr[j]=arr[j+1];
         arr[j+1]=temp;
     } 
  }
   }  
}
int main(){
 int arr[]={2,6,1,5,3,4};
 
 int n = sizeof(arr)/sizeof(arr[0]);
 //Perform Selection Sort 
 bubbleSort(arr,n);
 printf("\nSortted array through boubble sort:");
 for(int i=0;i<n;i++) 
   printf("%d ",arr[i]);
 return 0;     
 }


/*
#include<stdio.h>

//Selection sort implementtation
void selectionSort(int arr[],int n){
  for(int i=0; i < n-1;i++){
    int min =i;
    for(int j = i+1;j<n;j++){
      if(arr[j]<arr[min])
       min=j;
   }
  
  if(min!=i){
  int temp= arr[min];
  arr[min]=arr[i];
  arr[i]=temp;
 
  }
 }
}  
int main(){
  int arr[]={1,7,3,5,3,65};
  int n=sizeof(arr)/sizeof(arr[0]);
  //Perform selection sort
  printf("Sorted array through selection sort: ");
  for (int i=0;i<n;i++)
    printf("%d",arr[i]);
  return 0;  
}*/