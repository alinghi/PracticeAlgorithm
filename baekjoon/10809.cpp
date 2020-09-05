#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;


int main(void)
{
    string x;
    vector<int> p(26, -1);
    cin >> x;
    for (int i = 0; i < x.size(); i++) {
        if (p[x[i] - 'a']==-1) {
            p[x[i] - 'a'] = i;
        }
    }
    for (int i = 0; i < 26; i++) {
        cout << p[i] << " ";
    }
}