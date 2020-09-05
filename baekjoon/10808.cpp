#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;


int main(void)
{
    string x;
    vector<int> p(26, 0);
    cin >> x;
    for (int i = 0; i < x.size(); i++) {
        p[x[i] - 'a']++;
    }
    for (int i = 0; i < 26; i++) {
        cout << p[i] << " ";
    }
}