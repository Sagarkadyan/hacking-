#include<iostream>
int main(){
    int a,i,j;
    std::cin >> a;
    for(i=0; i <= a; i++)
    {
        for (j=0; j<=a ;j++)
        {
            std::cout<< a <<i<<j;
        }
    }
}