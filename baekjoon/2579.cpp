#include <iostream>
using namespace std;
#include <vector>

int max(int a, int b);

int main(void)
{
    int num, temp;

    cin >> num;
    vector<int> step;
    vector<int> dp(num, 0);
    for (int i = 0; i < num; i++) {
        cin >> temp;
        step.push_back(temp);
    }
    dp[0] = step[0];
    dp[1] = step[0] + step[1];
    dp[2] = max(step[0] + step[2], step[1] + step[2]);
    for (int i = 3; i < num; i++) {
        dp[i] = max(dp[i - 2] + step[i], step[i - 1] + step[i] + dp[i - 3]);
    }
    cout << dp[num-1] << endl;
    return 0;
}

int max(int a, int b) {
    if (a > b) return a;
    else return b;
}