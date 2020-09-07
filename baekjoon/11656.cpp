#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
bool mySort(string a, string b)
{
    if (a.compare(b) > 0)
        return false;
    else
        return true;
}

int main(void)
{
    string x;
    cin >> x;
    vector<string> p;
    for (int i = 0; i < x.size(); i++)
    {
        p.push_back(x.substr(i));
    }
    sort(p.begin(), p.end(), mySort);
    for (int i = 0; i < x.size(); i++)
    {
        cout << p[i] << endl;
    }
}