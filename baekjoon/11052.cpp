#include <iostream>
using namespace std;
#include <string>
#include <vector>

int main(void)
{
    int n, temp, max;
    cin >> n;
    vector<int> p;
    p.push_back(0);
    vector<unsigned long> dp(n+1, 0);
    for (int i = 0; i < n; i++) {
        cin >> temp;
        p.push_back(temp);
    }
    dp[0] = 0;
    dp[1] = p[1];
    for (int i = 2; i <= n; i++) {
        max = 0;
        for (int k = 1; k < i; k++) {
            if (max < dp[k] + dp[i - k]) max = dp[k] + dp[i - k];
        }
        if (max < p[i]) max = p[i];
        dp[i] = max;
    }
    cout << dp[n] << endl;
    return 0;
}
