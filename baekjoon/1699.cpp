#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
    int num, temp;
    cin >> num;
    vector<int> dp(100001, 0);
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    dp[4] = 1;
    dp[5] = 2;
    for (int i = 6; i <= num; i++) {
        for (int k = 1; k * k <= i; k++) {
            if (dp[i] > dp[i - k * k] + 1 || dp[i] == 0) {
                dp[i] = dp[i - k * k] + 1;
            }
        }
    }
    cout << dp[num] << endl;
    return 0;
}