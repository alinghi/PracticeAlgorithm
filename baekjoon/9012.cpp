#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;


int main(void)
{

    int num, temp;
    string x;
    bool y;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> x;
        y = true;
        vector<char> p;
        for (int j = 0; j < x.size(); j++) {
            if (x[j] == '(') {
                p.push_back('(');
            }
            else {
                if (p.size() == 0) y = false;
                else {
                    p.pop_back();
                }
            }
        }
        if (p.size() > 0) y = false;
        if (y) cout << "YES" << endl;
        else cout << "NO" << endl;

    }
    return 0;
}