#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    constexpr auto endl = "\n";
    int a, b, temp;
    vector<int> p;
    cin >> a >> b;
    for (int i = a; i <=b; i++) {
        p.push_back(i);
    }
    temp = 0;
    bool x;
    for (int i = 0; i < p.size(); i++) {
        x = true;
        if (p[i] == 0 || p[i] == 1) continue;
        else {
            for (int j = 2; j*j <= p[i]; j++) {
                if (p[i] % j == 0) x = false;
            }
            if (x) cout << p[i]<<endl;
        }
    }
}