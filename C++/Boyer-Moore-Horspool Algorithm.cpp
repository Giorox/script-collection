/*
	Boyer-Moore-Horspool Algorithm for text-in-text search
	Complexity: O(n)

    Implementation by: Giovanni Rebouças
    Universidade Federal de Itajubá - UNIFEI
	https://github.com/Giorox
    13/05/2016
*/
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

/*
	Function that returns the relative position of the first letter of the pattern in the text.
	
	@param string texto, where the search will take place; string padrão, what we are looking for
	@return int position of the first letter of what we are looking for in the text; If it's not found, return -1 by default
*/
int BMH(string texto, string padrao)
{
    int distpadrao[padrao.size()]; //Vector of word-distances

    for (int i = 0; i <padrao.size(); i++) //Defining the initial distances
    {
        if(i+1 == padrao.size())
            distpadrao[i] = padrao.size();
        else
            distpadrao[i] = padrao.size() - (1+i);
    }

    for (int i = 0; i <padrao.size(); i++) //Getting the min number of all distances to remove doubles
        for(int j = 0; j <padrao.size(); j++)
        {
            if(padrao[i] == padrao[j])
                if(distpadrao[i] < distpadrao[j])
                    distpadrao[j] = distpadrao[i];
                else
                    distpadrao[i] = distpadrao[j];
        }

    int pulo = 0; //Sets the jump variable to 0 initially

    while(texto.size() - pulo >= padrao.size()) //Certifies that the whole text will be read
    {
        int i = padrao.size() - 1; //Iterator that will be used to traverse the text
        bool contem = false;
        while(texto[pulo+i] == padrao[i]) //Checks if the pattern is found in the curren text position
        {
            if (i == 0)
                return pulo;
            i = i - 1;
        }

        for(int j = 0; j<=padrao.size(); j++) //Checks if any of the letters found match a position in the word-distance vector
        {
            if(texto[pulo+i] == padrao[j])
            {
                pulo = pulo + distpadrao[j];
                contem = true;
                break;
            }
        }
        if(contem == false) //If there isn't, jump will have the pattern's size added to it
            pulo = pulo + padrao.size();
    }
    return -1; //If it hasn't found anything, return -1, which means the pattern was not found in the text.
}

int main ()
{
    string texto, padrao;

    cout<<"Enter the text: ";
    getline(cin,texto);
    cout<<"Enter the pattern: ";
    getline(cin,padrao);

    int distancia = BMH(texto,padrao);

	if( distancia != -1 )
	{
		cout<<"The first letter of the pattern is in the " <<distancia <<" position of the text." <<endl;
		cout<<"Position: "<<texto <<endl;
		
		for(int i = 0; i < distancia+9; i++) //Prints a space character distance+9 times to input a "^" character to use as a visual reference to the user
			cout<<" ";
		cout<<"^";
	}
	else
		cout<<"The pattern was not found in the text.";

    return 0;
}
