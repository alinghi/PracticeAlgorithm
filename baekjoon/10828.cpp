#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;


int main(void)
{
    vector<int> p;
    int num, temp;
    string x;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> x;
        if (!x.compare("push")) {
            cin >> temp;
            p.push_back(temp);
        }
        else if (!x.compare("top")) {
            if (p.size() == 0) {
                cout << -1 << endl;
            }
            else {
                cout << p.back() << endl;
            }
        }
        else if (!x.compare("size")) {
            cout << p.size() << endl;
        }
        else if (!x.compare("empty")) {
            if (p.size() == 0) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
        else {
            //pop
            if (p.size() == 0) {
                cout << -1 << endl;
            }
            else {
                cout << p.back() << endl;
                p.pop_back();
            }
        }
    }
    return 0;
}