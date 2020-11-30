#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
    int n, temp;
    cin >> n;
    vector<int> input;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        input.push_back(temp);
    }
    vector<vector<int>> dp;
    dp.resize(n);
    for (int i = 0; i < n; i++)
    {
        dp[i].resize(3);
    }
    dp[0][0] = 0;
    dp[0][1] = input[0];
    dp[0][2] = 0;
    for (int i = 1; i < n; i++)
    {
        dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1], dp[i - 1][2]));
        dp[i][1] = dp[i - 1][0] + input[i];
        dp[i][2] = dp[i - 1][1] + input[i];
    }
    cout << max(dp[n - 1][0], max(dp[n - 1][1], dp[n - 1][2])) << endl;
    return 0;
}