#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;
bool mysort(pair<int, int> a, pair<int, int> b)
{
    if (a.second < b.second)
    {
        return true;
    }
    else if (a.second == b.second && a.first < b.first)
    {
        return true;
    }
    return false;
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
