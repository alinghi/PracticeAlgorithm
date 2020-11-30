#include <iostream>
#include <vector>
using namespace std;
vector<vector<long long>> dp;

int main(void)
{
    int tc;
    dp.resize(3);
    //0123
    dp[0].push_back(0);
    dp[0].push_back(1);
    dp[0].push_back(0);
    dp[0].push_back(1);
    dp[1].push_back(0);
    dp[1].push_back(0);
    dp[1].push_back(1);
    dp[1].push_back(1);
    dp[2].push_back(0);
    dp[2].push_back(0);
    dp[2].push_back(0);
    dp[2].push_back(1);
    cin >> tc;
    int temp;
    int current = 3;
    long long mod = 1000000009;
    for (int i = 0; i < tc; i++)
    {
        cin >> temp;
        if (current < temp)
        {
            for (int j = current + 1; j <= temp; j++)
            {
                current++;
                dp[0].push_back((dp[1][current - 1] + dp[2][current - 1]) % mod);
                dp[1].push_back((dp[0][current - 2] + dp[2][current - 2]) % mod);
                dp[2].push_back((dp[0][current - 3] + dp[1][current - 3]) % mod);
            }
            cout << ((dp[0][temp] + dp[1][temp] + dp[2][temp]) % mod) << endl;
        }
        else
        {
            cout << ((dp[0][temp] + dp[1][temp] + dp[2][temp]) % mod) << endl;
        }
    }
    return 0;
}