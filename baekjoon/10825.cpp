#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <tuple>
using namespace std;

bool mySort(tuple<string, int, int, int> a, tuple<string, int, int, int> b) {
    if (get<1>(a) > get<1>(b))	return true;
    else if (get<1>(a) == get<1>(b) && get<2>(a) < get<2>(b)) return true;
    else if (get<1>(a) == get<1>(b) && get<2>(a) == get<2>(b) && get<3>(a) > get<3>(b)) return true;
    else if (get<1>(a) == get<1>(b) && get<2>(a) == get<2>(b) && get<3>(a) == get<3>(b) && get<0>(a).compare(get<0>(b)) < 0) return true;
    return false;
}

int main(void)
{
    constexpr auto endl = "\n";
    vector<tuple<string, int, int, int>> p;
    int korean, english, math, n;
    string name;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> name >> korean >> english >> math;
        p.push_back(make_tuple(name, korean, english, math));
    }
    sort(p.begin(), p.end(), mySort);
    for (int i = 0; i < n; i++) {
        cout << get<0>(p[i])<<endl;
    }
    return 0;
}