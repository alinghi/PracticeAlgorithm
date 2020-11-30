#include <iostream>
#include <vector>
using namespace std;
int main(void)
{
    vector<int> v;
    v.push_back(0);
    v.push_back(1);
    v.push_back(2);
    v.push_back(4);
    for (int i = 0; i < 11; i++)
    {
        v.push_back(v[v.size() - 1] + v[v.size() - 2] + v[v.size() - 3]);
    }
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i++)
    {
        int temp;
        cin >> temp;
        cout << v[temp] << endl;
    }
    return 0;
}