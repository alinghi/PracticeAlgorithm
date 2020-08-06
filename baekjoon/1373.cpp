#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    string x;
    vector<int> p;
    int cnt = 1;
    int temp = 0;
    cin >> x;
    for (int i = 0; i < x.size()/3; i++) {
        temp = 0;
        temp += (x[x.size() - 1 - 3 * i-0]-'0')*1;
        temp += (x[x.size() - 1 - 3 * i-1]-'0')*2;
        temp += (x[x.size() - 1 - 3 * i-2]-'0')*4;
        p.push_back(temp);
    }
    if (x.size() % 3 == 1) {
        temp = 0;
        temp += (x[0] - '0') * 1;
        p.push_back(temp);
    }
    else if (x.size() % 3 == 2) {
        temp = 0;
        temp += (x[1] - '0') * 1;
        temp += (x[0] - '0') * 2;
        p.push_back(temp);
    }
    for (int i = 0; i < p.size(); i++) {
        cout << p[p.size() - 1 - i];
    }
}