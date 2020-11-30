#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int main(void)
{
    cin >> N;
    int temp;
    vector<int> input;
    vector<int> dp;
    vector<int> root;
    vector<int> ans;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        input.push_back(temp);
    }
    dp.resize(N);
    root.resize(N);
    for (int i = 0; i < N; i++)
    {
        dp[i] = 1;
        root[i] = -1;
        for (int j = 0; j < i; j++)
        {
            if (input[j] < input[i] && dp[i] < dp[j] + 1)
            {
                dp[i] = dp[j] + 1;
                root[i] = j;
            }
        }
    }
    int t = distance(dp.begin(), max_element(dp.begin(), dp.end()));
    cout << dp[t] << endl;
    do
    {
        ans.push_back(input[t]);
        t = root[t];
    } while (t != -1);
    for (vector<int>::reverse_iterator it = ans.rbegin(); it != ans.rend(); it++)
    {
        cout << *it << " ";
    }
    return 0;
}