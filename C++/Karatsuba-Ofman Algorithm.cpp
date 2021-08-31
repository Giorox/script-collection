/*
    Karatsuba-Ofman Algorithm for fast big integer multiplication
	Complexity: O(n^log3)
	
	Implementation by: Giovanni Rebouças
    Universidade Federal de Itajubá - UNIFEI
	https://github.com/Giorox
    22/04/2017
*/
#include <iostream>
#include <cmath>
using namespace std;

/*
	Function that returns the multiplication of 2 integers of size n
	
	@param int u, first integer; int v, second integer; int n, integer size
	@return int multiplication result of u and v
*/
int KaratsubaOfman (int u, int v, int n)
{
    if (n < 3)
        return u*v;
    else
    {
        int m = n/2;
        int p = u/pow(10,m);
        int q = u*pow(10,m);
        int r = v/pow(10,m);
        int s = v*pow(10,m);
        int pr = KaratsubaOfman (p, r, m);
        int qs = KaratsubaOfman (q, s, m);
        int y = KaratsubaOfman (p+q, r+s, m+1);
        int x = (pr*pow(10,2*m)) + ((y-pr-qs)*pow(10,m)) + qs;
        return  x;
    }
}

int main()
{
    int u = 10, v = 11, n = 2;

    cout <<KaratsubaOfman(u, v, n);
}
