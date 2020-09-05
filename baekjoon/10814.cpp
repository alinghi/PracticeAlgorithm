#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <tuple>
using namespace std;
bool mysort(tuple<int, int, string> a, tuple<int, int, string> b) {
    if (get<0>(a) < get<0>(b)) {
        return true;
    }
    else if (get<0>(a) == get<0>(b) && get<1>(a) < get<1>(b)) {
        return true;
    }
    return false;
}
int main(void)
{
    constexpr auto endl = "\n";
    int n, temp1;
    string temp2;

    vector<tuple<int, int, string>> p;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> temp1 >> temp2;
        p.push_back(make_tuple(temp1, i, temp2));
    }
    sort(p.begin(), p.end(), mysort);
    for (int i = 0; i < n; i++) {
        cout << get<0>(p[i]) << " " << get<2>(p[i]) << endl;

    }
    return 0;
}
