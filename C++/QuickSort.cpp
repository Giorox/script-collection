#include <iostream>
#include <cstdio>;
#define NUM 1000000000000
#include <stdlib.h>
#include<time.h>
using namespace std;

int partition(int arr[], int low, int high);

void quickSort(int arr[], int low, int high){
    if(low<high)
    {
        int pi = partition(arr, low,high);
        quickSort(arr,low,pi-1);
        quickSort(arr,pi+1,high);
    }
}

void printArray(int arr[], int size){
    int i;
    for(i=0;i<size;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[NUM];

    srand(time(NULL));

    for(int i=NUM;i>=(NUM/2);i--)
    {
        arr[i] = rand()%100000;
    }
    for(int i=0;i<=(NUM/2);i++)
    {
        arr[i] = rand()%100000000;
    }
    quickSort(arr,0,NUM+1);
    //printArray(arr,NUM+1);
    return 0;
}


void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

int partition(int arr[], int low, int high){
    int pivot = arr[high];
    int i=low-1;
    for(int j=low;j<=high;j++){
        if(arr[j]<pivot){
            i++;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[high]);
    return i+1;
}
