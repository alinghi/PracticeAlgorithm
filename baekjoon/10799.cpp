#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;


int main(void)
{
    string x;
    cin >> x;
    vector<char> p;
    bool y=false;
    unsigned long long ans=0;
    for (int i = 0; i < x.size(); i++) {
        if (x[i] == '(') {
            //open bracket
            p.push_back('(');
            y = true;
        }
        else {
            p.pop_back();
            //laser
            if (x[i - 1] == '(') {
                ans += p.size();
            }
            else {
                ans++;
            }

        }
    }
    cout << ans <<endl;
    return 0;
}