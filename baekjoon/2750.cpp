#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
int main(void)
{
    int n, temp;
    cin >> n;
    vector<int> p;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        p.push_back(temp);
    }
    sort(p.begin(), p.end());
    for (int i = 0; i < n; i++) {
        cout << p[i] << endl;

    }
    return 0;
}
