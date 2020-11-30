#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int tc;
    cin >> tc;
    int l;
    int temp;
    vector<int> x1;
    vector<int> x2;
    vector<vector<int>> dp;
    for (int i = 0; i < tc; i++)
    {
        cin >> l;
        x1.clear();
        x2.clear();
        dp.clear();
        dp.resize(3);
        for (int j = 0; j < l; j++)
        {
            cin >> temp;
            x1.push_back(temp);
        }
        for (int j = 0; j < l; j++)
        {
            cin >> temp;
            x2.push_back(temp);
        }
        dp[0].push_back(0);
        dp[1].push_back(x2[0]);
        dp[2].push_back(x1[0]);
        for (int k = 0; k < l - 1; k++)
        {
            dp[0].push_back(max(dp[0][k], max(dp[1][k], dp[2][k])));
            dp[1].push_back(max(dp[0][k], dp[2][k]) + x2[k + 1]);
            dp[2].push_back(max(dp[0][k], dp[1][k]) + x1[k + 1]);
        }
        cout << max(dp[0][l - 1], max(dp[1][l - 1], dp[2][l - 1])) << endl;
    }
    return 0;
}