#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <tuple>
using namespace std;

int main(void)
{
    constexpr auto endl = "\n";
    long long n, temp;
    vector<long long> p;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        p.push_back(temp);
    }
    sort(p.begin(), p.end());
    long long count = 0;
    long long prev_count = 0;
    long long freq = p[0];
    for (long long i = 1; i < n; i++)
    {
        if (p[i] == p[i - 1])
        {
            count++;
            if (count > prev_count)
            {
                freq = p[i];
                prev_count = count;
            }
        }
        else
        {
            count = 0;
        }
    }
    cout << freq << endl;
    return 0;
}
