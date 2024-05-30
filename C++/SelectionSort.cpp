/*
Selection sort
for i = 1:n,
    k = i
    for j = i+1:n, if a[j] < a[k], k = j
    → invariant: a[k] smallest of a[i..n]
    swap a[i,k]
    → invariant: a[1..i] in final position
end
*/


#include <iostream>
#define NUM 1000000000
#include <stdlib.h>
#include<time.h>

typedef unsigned int UINT;

void selectionSort(int array[], UINT size)
{
    // first iteration to find the lowest value
  for (UINT i = 0; i < size; i++)
  {
    if (array[0] > array[i])
    {
      int temp = array[0];
      array[0] = array[i];
      array[i] = temp;
    }
  }

  for (UINT i = 1; i < size; i++)
  {
    for (UINT j = i+1; j < size; j++)
    {
      if (array[i] > array[j])
      {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }
}
int main()
{
  int test[NUM];

  srand(time(NULL));

    for(int i=NUM;i>=(NUM/2);i--)
    {
        test[i] = rand()%10000000;
    }
    for(int i=0;i<=(NUM/2);i++)
    {
        test[i] = rand()%100000000;
    }

  UINT usize  = sizeof(test) / sizeof(test[0]);
  selectionSort(test, usize);


  //for (UINT i = 0; i < usize; ++i)
  //{
  //  std::cout << test[i] << " ";
  //}

  return 0;
}
