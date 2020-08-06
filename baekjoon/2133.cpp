#include <iostream>
using namespace std;
#include <vector>

int main(void)
{
    int num, temp;
    cin >> num;
    if (num % 2 == 1) {
        cout << 0 << endl;
    }
    else {
        vector<int> dp(30, 0);
        dp[0] = 1;
        dp[2] = 3;
        for (int i = 4; i <= num; i = i + 2) {
            dp[i] = dp[i - 2] * 3;
            for (int k = 4; i - k >= 0; k = k + 2) {
                dp[i] += dp[i - k] * 2;
            }
        }
        cout << dp[num] << endl;
    }
    return 0;
}
