#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
    int n, k, index;
    cin >> n >> k;
    vector<int> p;

    for (int i = 1; i <= n; i++) {
        p.push_back(i);
    }
    index = 0;
    cout << "<";
    for (int i = 0; i < n; i++) {
        index = (index + k - 1) % p.size();
        if (p.size() != 1)	cout << p[index] << ", ";
        else cout << p[index];
        p.erase(p.begin()+index);
    }
    cout << ">";
    return 0;
}