#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    int num, temp;
    vector<int> p;
    cin >> num;
    for (int i = 0; i < num; i++) {
        cin >> temp;
        p.push_back(temp);
    }
    temp = 0;
    bool x;
    for (int i = 0; i < num; i++) {
        x = true;
        if (p[i] == 0 || p[i] == 1) continue;
        else {
            for (int j = 2; j < p[i]; j++) {
                if (p[i] % j == 0) x = false;
            }
            if (x) temp++;
        }
    }
    cout << temp;
}