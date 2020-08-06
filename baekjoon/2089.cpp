#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    long long int x;
    cin >> x;
    vector<int> p;
    long long int temp=1;
    while (x != 0) {
        if (x % 2 == 0) {
            p.push_back(0);
            x = (-x) / 2;
        }
        else {
            p.push_back(1);
            x = -(x - 1) / 2;
        }
    }
    if (!p.size()) cout << 0;
    else for (int i = 0; i < p.size(); i++) cout << p[p.size()-1-i];
    return 0;
}