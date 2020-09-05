#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    unsigned long long int n;
    int b;
    vector<int> p;
    cin >> n >> b;
    while (n != 0) {
        p.push_back(n % b);
        n = n / b;
    }
    for (int i = 0; i < p.size(); i++) {
        if (p[p.size() - 1 - i] < 10) cout << p[p.size() - 1 - i];
        else cout << (char)(p[p.size() - 1 - i] + 'A' - 10);
    }
}