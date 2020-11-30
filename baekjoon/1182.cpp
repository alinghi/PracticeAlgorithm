#include <iostream>
#include <vector>
using namespace std;
vector<int> x;
int main(void)
{
    int N, M;
    cin >> N >> M;
    int temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        x.push_back(temp);
    }
    int ans = 0;
    for (int i = 1; i < (1 << N); i++)
    {
        int sum = 0;
        for (int j = 0; j < N; j++)
        {
            if (i & (1 << j))
            {
                sum += x[j];
            }
        }
        if (sum == M)
        {
            ans++;
        }
    }
    cout << ans;
    return 0;
}