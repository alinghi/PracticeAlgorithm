#include <iostream>
using namespace std;
#include <string>
#include <vector>

int main(void)
{
    string line;
    int current, prev, temp, start;
    vector<long> dp(5002, 0);
    getline(cin, line);
    dp[0] = dp[1] = 1;
    if (line[0] == '0') {
        cout << 0 << endl;
        return 0;
    }
    for (int i = 2; i < line.length()+1; i++) {
        current = line[i - 1]-'0';
        prev = line[i - 2] - '0';
        temp = 10 * prev + current;
        if (current > 0) dp[i] = dp[i - 1];
        if (temp >= 10 && temp <= 26) dp[i] += dp[i - 2] % 1000000;

    }
    cout << dp[line.length()] % 1000000 << endl;
    return 0;
}
