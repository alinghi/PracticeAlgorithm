#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool check(vector<char> &order, vector<int> &c)
{
    for (int i = 0; i < order.size(); i++)
    {
        if (order[i] == '<' && c[i] > c[i + 1])
        {
            return false;
        }
        if (order[i] == '>' && c[i] < c[i + 1])
        {
            return false;
        }
    }
    return true;
}

int main(void)
{
    int n;
    cin >> n;
    vector<int> big;
    for (int i = 9 - n; i < 10; i++)
        big.push_back(i);
    vector<int> small;
    for (int i = 0; i < n + 1; i++)
        small.push_back(i);
    vector<char> order;
    char c;
    for (int i = 0; i < n; i++)
    {
        cin >> c;
        order.push_back(c);
    }
    vector<int> big_ans;
    do
    {
        if (check(order, big))
        {
            big_ans = big;
        }
    } while (next_permutation(big.begin(), big.end()));
    vector<int> small_ans;
    reverse(small.begin(), small.end());
    do
    {
        if (check(order, small))
        {
            small_ans = small;
        }
    } while (prev_permutation(small.begin(), small.end()));
    for (auto it : big_ans)
    {
        cout << it;
    }
    cout << endl;
    for (auto it : small_ans)
    {
        cout << it;
    }
    return 0;
}