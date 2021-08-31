#include <iostream>
#include <stdlib.h>
#include<time.h>
using namespace std;
#define NUM 1000000000

int main()
{
    int array1[NUM] = {0};

    srand(time(NULL));

    for(int i=NUM;i>=(NUM/2);i--)
    {
        array1[i] = rand()%100000;
    }
    for(int i=0;i<=(NUM/2);i++)
    {
        array1[i] = rand()%100000000;
    }
    //bubble sort
    for(int i=0;i<=NUM;i++)
    {
        for(int j=0+i;j<=NUM;j++)
        {
            if(array1[i]>array1[j])
            {
               int x=array1[i];
               array1[i]=array1[j];
               array1[j]=x;
            }
        }
    }

     //for(int i=0;i<=NUM;i++)
     //{
     //   cout<<array1[i]<<" ";
     //}
    return 0;
}
