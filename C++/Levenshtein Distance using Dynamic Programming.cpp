/*
    Levenshtein Distance using Dynamic Programming
	Complexity: O(n^2-x) where x is an integer smaller than 0
	
	Implementation by: Giovanni Rebouças
    Universidade Federal de Itajubá - UNIFEI
	https://github.com/Giorox
    22/04/2017
*/
#include <iostream>
using namespace std;

/*
	Funnction that returns the number of single-digit operations (insertion, deletion and substitution) necessary to transform one string into the other
	
	@param string s, first string; string t, second string; int m, size of the s string; int n, size of the t string
	@return int the number of operations necessary to turn the "s" string into the "t" string
*/
int algoritmoPD(string s, string t, int m, int n)
{
    int d[m][n];
    int i, j, subst;

    for(i=0; i <= m; i++)
        for(j=0; j <= n; j++)
            d[i][j] = 0;

    for(i = 1; i<=m; i++)
        d[0][i] = i;

    for(j = 1; j <= n; j++)
        d[j][0] = j;

    for(j = 1; j <= n; j++)
        for(i=1; i<= m; i++)
        {
            if(s[i] == t[j])
                subst = 0;
            else
                subst = 1;

            d[i][j] =std::min(std::min(d[i-1][j] + 1, d[i][j-1] + 1), d[i-1][j-1] + subst);
        }
    return d[m][n];
}

int main ()
{
    int m = 0, n = 0;
    string s, t;

    cin>>s;
    cin>>t;

    m = s.size();
    n = t.size();

    cout<<"RESULTADO: " <<algoritmoPD(s, t, m, n);

    return 0;
}
