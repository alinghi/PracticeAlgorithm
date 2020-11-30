#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    vector<int> x;
    x.resize(N);
    int temp;
    for (int i = 0; i < N; i++)
    {
        cin >> temp;
        x[i] = temp;
    }
    int left = 0;
    int right = 0;
    int sum = x[0];
    int ans = 0;
    while (left <= right && right < N)
    {
        if (sum < M)
        {
            right += 1;
            sum += x[right];
        }
        else if (sum == M)
        {
            ans += 1;
            right += 1;
            sum += x[right];
        }
        else if (sum > M)
        {
            sum -= x[left];
            left++;
            if (left > right && left < N)
            {
                right = left;
                sum = x[left];
            }
        }
    }
    cout << ans;
    return 0;
}