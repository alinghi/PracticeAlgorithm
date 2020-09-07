#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
bool mysort(pair<int, int> a, pair<int, int> b)
{
    if (a.first > b.first)
    {
        return false;
    }
    else if (a.first == b.first && a.second > b.second)
    {
        return false;
    }
    return true;
}
int main(void)
{
    constexpr auto endl = "\n";
    int n, temp1, temp2;
    vector<pair<int, int>> p;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> temp1 >> temp2;
        p.push_back(make_pair(temp1, temp2));
    }
    sort(p.begin(), p.end(), mysort);
    for (int i = 0; i < n; i++)
    {
        cout << p[i].first << " " << p[i].second << endl;
    }
    return 0;
}
