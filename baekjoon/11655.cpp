#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int main(void)
{
    string x;
    getline(cin, x);
    for (int i = 0; i < x.size(); i++)
    {
        if (x[i] >= 'a' && x[i] <= 'z')
        {
            cout << (char)((x[i] - 'a' + 13) % 26 + 'a');
        }
        else if (x[i] >= 'A' && x[i] <= 'Z')
        {
            cout << (char)((x[i] - 'A' + 13) % 26 + 'A');
        }
        else
        {
            cout << (char)(x[i]);
        }
    }
}